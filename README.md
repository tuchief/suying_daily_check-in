# suying666_checkin
suying666 autocheck in daily to get traffic

## 功能介绍
1、suying666每日自动签到  
2、通过Bark推送签到和会员信息，包含当日签到获取的流量、会员剩余时长、剩余流量、连接设备、公告信息

## chromedriver下载地址
https://chromedriver.storage.googleapis.com/index.html  
https://npm.taobao.org/mirrors/chromedriver

## 安装
1、install python3 
2、install pip
3、`pip install selenium`
4、根据部署的环境中的Chrome版本的不同，下载安装不同的chrome
5、安装Chromedriver驱动
6、修改运行文件`suying_checkin.py`内的需要修改的部分

## 使用方法
在对应的操作系统上配置定时任务来运行 `python suying_checkin.py`

by windows  
suying_checkin.bat文件是为Windows的任务计划设置而准备的  
可以使用windows的任务计划来自动每天定时来完成签到

by linux
crontab -e 
30 0 *  *  * python ..../suying_checkin.py

## 效果预览
![]()

