import urllib.request
import time

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')]


def get_valid_url():
    """
    检查URL 列表有效性，获取可访问的URL立即返回
    :return:
    """
    print("开始校验并获取最近一个可访问的URL...")
    file = open('urls.txt')
    lines = file.readlines()

    url_list = []
    for line in lines:
        url = line.replace('\n', '')
        url_list.append(url)

    final_url = ""
    for url in url_list:
        tempUrl = url
        try:
            opener.open(url)
            final_url = url
            break
        except urllib.error.HTTPError:
            time.sleep(2)
        except urllib.error.URLError:
            time.sleep(2)
        time.sleep(1)
    print("校验完成！URL： " + final_url)
    return final_url
