# suying666_checkin
suying666 每日自动签到、会员账户、公告等信息推送

## 功能介绍
- 每日自动签到获取免费流量  
- 从URL列表文件中，自动检测可访问的URL进行登录
- 每日通过Bark推送签到和会员信息，内容包含当日签到获取的流量、会员剩余时长、剩余流量、连接设备、公告信息  
- 抓取公告中的备用地址，自动更新URL列表文件  

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
在对应的操作系统上配置定时任务来运行  
`python suying_checkin.py`  

by windows  
`suying_checkin.bat`文件是为Windows的任务计划设置而准备的  
可以使用windows的任务计划来自动每天定时来完成签到

by linux  
`crontab -e`  
`30 0 *  *  * python ..../suying_checkin.py`

## 效果预览
![](https://github.com/tuchief/suying666_checkin/blob/main/image2.png)
![](https://github.com/tuchief/suying666_checkin/blob/main/image1.png)

## 免责说明
- 本项目仅供个人学习RPA技术参考使用。用户明确同意其使用本开源项目所存在的风险将完全由其自己承担；因其使用本项目而产生的一切后果也由其自己承担，开源作者对用户不承担任何责任。  
- 任何由于使用本开源项目而造成的个人资料泄露、丢失、被盗用或被窜改及由此而导致的任何法律争议和后果等，本开源均得免责。  
- 开源使用者因使用本项目而触犯中华人民共和国法律的，一切后果自己负责，开源作者不承担任何责任。
- 凡以任何方式获取本开源项目代码或直接、间接使用本开源资料者，视为自愿接受本开源声明的约束。
- 声明未涉及的问题参见国家有关法律法规，当本声明与国家法律法规冲突时，以国家法律法规为准。  
