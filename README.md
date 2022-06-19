

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
          USERNAME: ${{ secrets.USERNAME }}       # 学号
          PASSWORD: ${{ secrets.PASSWORD }}       # 信息门户密码
          AREA: ${{ secrets.AREA }}               # 所在地区，例如例如"北京市 海淀区"，用空格号隔开
          PROVINCE: ${{ secrets.PROVINCE }}       # 所在省份，例如"北京市"
          CITY: ${{ secrets.CITY }}               # 所在城市，例如"北京市"
          SFZX: ${{ secrets.SFZX }}               # 是否在校，填"1"表示在校，"0"表示不在
  ```

3. 根据2中env的变量，在仓库的Settings-->Secrets中添加对应的值

   ![image-20220109211120815](https://images.xiaoniuren666.com/img/image-20220109211120815.png)

   依次将USERNAME、PASSWORD、AREA、PROVINCE、CITY、SFZX等环境变量添加进去

   以USERNAME为例：

   ![image-20220109205823048](https://images.xiaoniuren666.com/img/image-20220109205823048.png)

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

6. 记得每60天要更新下～～
