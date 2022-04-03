

# 北邮每日填报自动化

北邮自动疫情打卡

## 说明
利用Github提供的Actions完成自动运行脚本的过程
在`.github/workflow`中有一个YAML文件，打开后即可查看自动运行的相关细节

## 操作说明
1. 点击右上角的Fork将本仓库拷贝到自己的仓库中

2. 打开自己Fork的仓库，查看`.github/workflows/main.yml`中env的字段，如下

  ``` yaml
  env:
          USERs: ${{ secrets.USERs }}       # (学号,密码,server昵称，是否在校) # 是否在校，填"1"表示在校，"0"表示不在
          PASSWORD: ${{ secrets.PASSWORD }}       # 信息门户密码
          AREA: ${{ secrets.AREA }}               # 所在地区，例如例如"北京市 海淀区"
          PROVINCE: ${{ secrets.PROVINCE }}       # 所在省份，例如"北京市"
          CITY: ${{ secrets.CITY }}               # 所在城市，例如"北京市"
          SERVER_KEY: ${{ secrets.SERVER_KEY }}   # server酱的发送key
  ```

3. 根据2中env的变量，在仓库的Settings-->Secrets中添加对应的值

   ![image-20220109211120815](https://images.xiaoniuren666.com/img/image-20220109211120815.png)

   依次将USERs、AREA、PROVINCE、CITY等环境变量添加进去

  ``` yaml
       USERs: [('20********','key','nickname',0)]
       AREA: ["北京市 海淀区"]
       PROVINCE: ["北京市"]
       CITY: ["北京市"]
       SERVER_KEY: *********
  ```
  
4. 在添加完毕后，点击Actions，进入自动操作的提示界面，开启Workflows

5. 自动操作的触发条件有二，在`.github/workflows/main.yml`中有说明

   ``` yaml
   on:
     push:
       branches: [ main ]
     schedule:
       - cron: '0 1 * * *'
       - cron: '0 17 * * *'
   #原来设置的时间是UTC时间的每日1:00 AM，即China Time的9:00 AM
   #但是因为近期Actions出现波动，导致很多人没打上卡，现在增加UTC时间的17:00(China Time次日1:00)
   ```

6. 记得每60天要更新下～

7. 关于server 酱

  有关于多人的server发送暂未适配，所以目前使用单server发送

  有关于server酱的自定义只有显示名称 name，可以在程序中的NAME设置

  secret的Name填写**SERVER_KEY**(SERVER_KEY的填写如下）

  如果不配置Server酱微信推送，那么Value里填写**0**即可，如果想配置的话看下一点

  **（可选）** Value填写Server酱的SendKey（在这里查看 [https://sct.ftqq.com/sendkey](https://sct.ftqq.com/sendkey)），在此之前需要微信注册企业号，并加入Server酱内部应用，具体流程见 [https://sct.ftqq.com/forward](https://sct.ftqq.com/forward)，看起来比较多，但也不是很麻烦，一步步照做即可
