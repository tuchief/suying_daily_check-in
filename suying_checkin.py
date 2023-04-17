from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os
from selenium.webdriver.support.ui import WebDriverWait
import requests
from urllib import parse
from check_url import get_valid_url, update_urls
from selenium.webdriver.common.by import By

os.system("killall -9 chrome")
os.system("killall -9 chromedriver")

# ============== 以下内容按需修改
# 登录邮箱
email = "登录邮箱"
# 登录密码
password = "登录密码"
# 通知标题
notice_title = "速鹰666签到"
# Bark服务推送地址，可以更换为 PushDeer 或者 Server酱
notice_objects = [
    # myself
    "https://api.day.app/token1"
    # 郭伟斌
    ,"https://api.day.app/token2"
    # 郭伟斌朋友 咔咔、
    ,"https://api.day.app/token3"
]
# 推送公告内容最大字数，超过部分用...表示
notice_words_max = 200
# ==============

# 获取可访问的URL地址
page_url = get_valid_url()
if page_url == "":
    full_notice = "很抱歉，没有找到可访问URL，请手动登录网站查询最新地址，并更新到urls.txt文件中"
    for notice_object in notice_objects:
        r = requests.get(notice_object + "/" + notice_title + "/" + parse.quote(full_notice, safe=''))
        print(r.json())
    exit(-1)

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

print("初始化浏览器完成，正在打开页面 " + page_url)
driver.get(page_url)

# 1、登录界面
driver.implicitly_wait(60)
print("——" +driver.title)
# 输入邮箱
time.sleep(1)
print('————输入邮箱')
driver.find_element(By.ID,'email').send_keys(email)
# 输入密码
time.sleep(1)
print('————输入密码')
driver.find_element(By.ID,'password').send_keys(password)
# 点击登录
time.sleep(1)
print('————点击登录')
driver.find_element(By.CLASS_NAME,'login').click()

# 2、签到

print("——等待登录完成")
driver.implicitly_wait(60)

print("——登录完成，开始签到")
# 登录完成，等待页面加载完成
WebDriverWait(driver, 60).until(lambda driver: driver.find_element(By.ID,"checkin-div"))
# 刷新当前页面，避免页面出现公告弹出框而导致后续操作无法继续（刷新后公告弹出框当天不会再次出现）
driver.refresh()
# 今日是否已签到
button_text = driver.find_element(By.ID,'checkin-div').text
# 签到结果
check_result = ''
if button_text == '明日再来':
    print("————今日已签到，明日再来")
    check_result = 'ㄟ(▔,▔)ㄏ 今日已签到，明日再来'
else:
    print("————点击签到按钮")
    driver.find_element(By.ID,'checkin-div').click()
    WebDriverWait(driver, 60).until(lambda driver: driver.find_element(By.ID,"swal2-content"))
    time.sleep(1)
    check_result = "╰(￣▽￣)╭" + driver.find_element(By.ID,'swal2-content').text
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/button[1]').click()

# 3、会员相关信息

print('——获取会员相关信息')
time.sleep(5)
# 会员剩余时长
vip_remaining_time = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/section/div[2]/div[1]/div/div[2]/div[2]/span').text
print("————会员剩余时长：" + vip_remaining_time)

# 剩余流量
residual_flow_and_unit = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div/div[2]/div[2]').text
print("————剩余流量：" + residual_flow_and_unit)

# 在线设备
current_connected = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/section/div[2]/div[3]/div/div[2]/div[2]/span[1]').text
sum_connect = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/section/div[2]/div[3]/div/div[2]/div[2]/span[2]').text
print("————在线设备：" + current_connected + "/" + sum_connect)

# 公告
print('——公告')
notice = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/section/div[3]/div[1]/div/div[2]').text
notice_len = len(notice)
if notice_len > notice_words_max:
    notice = notice[0:notice_words_max] + "..."
print("————公告：" + notice)

full_notice = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) \
              + "\n" + check_result \
              + "\n\n" + "会员剩余时长：" + str(vip_remaining_time) + " 天" \
              + "\n" + "剩余流量：" + str(residual_flow_and_unit) \
              + "\n" + "在线设备：" + str(current_connected) + "/" + str(sum_connect) \
              + "\n" + str(notice)

# 推送通知
print('——推送通知')
for notice_object in notice_objects:
    r = requests.get(notice_object + "/" + notice_title + "/" + parse.quote(full_notice, safe=''))
    print(r.json())

# 获取备用网址，更新到urls.txt文件中
print('——更新URL地址文件')
urls = []
url_list_el = driver.find_elements(By.XPATH,"//*[contains(@href,'https://suying')]")
for url_el in url_list_el:
    urls.append(url_el.text)
# 更新到url文件中
update_urls(urls)

time.sleep(3)
driver.quit()




