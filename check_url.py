import urllib.request
import time

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]
# 存储url列表的文件名
file_name = 'urls.txt'


def update_urls(urls):
    """
    更新url列表
    :param url_list:
    :return:
    """
    if len(urls) == 0:
        print("没有要更新的URL记录")
        pass
    with open(file_name, 'w+') as f:
        for url in urls:
            f.write(url.strip() + "\n")
        f.flush()
    print("新更新URL记录 " + str(len(urls)) + " 条")


def get_valid_url():
    """
    检查URL 列表有效性，获取可访问的URL立即返回
    :return:
    """
    print("开始校验并获取最近一个可访问的URL...")
    url_list = []
    with open(file_name, 'r') as f:
        url_list = f.readlines()

    final_url = ""
    for url in url_list:
        print(url, end=" -> ")
        try:
            opener.open(url)
            final_url = url
            print("可用\n",)
            break
        except urllib.error.HTTPError:
            print("不可用\n")
            time.sleep(2)
        except urllib.error.URLError:
            print("不可用\n")
            time.sleep(2)
        time.sleep(1)
    print("校验完成！URL： " + final_url)
    return final_url
