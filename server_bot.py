import time
import requests,datetime

# from typing import Optional
from abc import ABCMeta, abstractmethod

class INotifier(metaclass=ABCMeta):
    @property
    @abstractmethod
    def PLATFORM_NAME(self) -> str:
        """
        将 PLATFORM_NAME 设为类的 Class Variable，内容是通知平台的名字（用于打日志）。
        如：PLATFORM_NAME = 'Telegram 机器人'
        :return: 通知平台名
        """
    @abstractmethod
    def notify(self, *, success, msg, data,username, name) -> None:
        """
        通过该平台通知用户操作成功的消息。失败时将抛出各种异常。
        :param success: 表示是否成功
        :param msg: 成功时表示服务器的返回值，失败时表示失败原因；None 表示没有上述内容
        :return: None
        """

import os        
USERs = eval(os.environ['USERs'])
TIMEOUT_SECOND = 25

class ServerJiangNotifier(INotifier):
    PLATFORM_NAME = 'Server 酱'

    def __init__(self, *, sckey: str, sess: requests.Session):
        self._sckey = sckey
        self._sess = sess

    def notify(self, *, success, msg, data, username, name) -> None:
        """发送消息。"""
        title_suc,title_eor,bodys=[],[],[]
        title_suc_str,title_eor_str,body_str='','',''

        for i in range(len(USERs)):
            if success[i]:
                title_suc += [f'{name[i]}']
                if msg[i] is not None:
                    body = f'\n学号{username[i]},{name[i]}\n填报位置:\n{data[i]}\n 填报成功, 服务器的返回是:\n{msg[i]}\n'
                else:
                    body = '成功'
            else:
                title_eor += [f'{name[i]}']
                if msg[i] is not None:
                    body = f'学号{username[i]}\n填报位置:\n{data[i]}\n 填报失败：产生如下异常：\n{msg[i]}\n'
                else:
                    body = '失败'
            bodys+=[body]
        
        for i in range(len(title_suc)):
            title_suc_str+=title_suc[i]
            if i!= len(title_suc)-1:
                title_suc_str+='、'
            else:
                title_suc_str+="填报成功!"

        if len(title_eor)==0:
            title_suc_str="所有填报成功"

        for i in range(len(title_eor)):
            title_eor_str+=title_eor[i]
            if i!= len(title_eor)-1:
                title_eor_str+='、'
            else:
                title_eor_str+="填报失败!"

        for i in range(len(bodys)):
            body_str+=bodys[i]
        
        # Server 不允许短时间重复发送相同内容，故加上时间
        time_str = str(int(time.time()))[-3:]

        # 调用 Server 酱接口发送消息
        sc_res_raw = self._sess.post(
            f'https://sctapi.ftqq.com/{self._sckey}.send',
            data={
                'title': f'{datetime.date.today()}:{title_suc_str}{title_eor_str}',
                'desp': f'{body_str}',
            },
            timeout=TIMEOUT_SECOND,
        )
