"""
获取微信西樵漫画头像
"""
import requests  # 导入requests 模块
from bs4 import BeautifulSoup  # 导入BeautifulSoup 模块
import os  # 导入os模块

import time


def datetimestr():
    '''''
    get datetime string
    date format="YYYYMMDDHHMMSS"
    '''
    return year + mon + day + hour + min + sec


class BeautifulPicture():

    # 类的初始化操作
    def __init__(self):
        # 给请求指定一个请求头来模拟chrome浏览器
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}
        self.web_url = 'https://mp.weixin.qq.com/s/vHq09ExVR_XMSR3l8z9YcA'
        # 要访问的网页地址
        self.web_urls = ('http://mp.weixin.qq.com/s/fbwR_DafXH6Zc8gZmrYxHQ',
                         'http://mp.weixin.qq.com/s/c9W79k_JMwG4PQ4hRIfXsg',
                         'http://mp.weixin.qq.com/s/vlyDd546w4XwPmW0nFFVAg',
                         'https://mp.weixin.qq.com/s/keuvuF9GYKSHH6U-RpK6Ig',
                         'http://mp.weixin.qq.com/s/vHq09ExVR_XMSR3l8z9YcA')
        # 设置图片要存放的文件目录
        self.folder_path = 'D:\BeautifulPicture\wx'

    def get_pic(self):
        for web_url in self.web_urls:
            print('开始网页get请求')
            r = self.request(web_url)
            print('开始获取所有img标签')
            # 获取网页中的class为cV68d的所有a标签 , '[data-s="300,640"]'
            all_a = BeautifulSoup(r.text, 'lxml').find_all('img', attrs={
                "data-s": "300,640"})
            #print(all_a)
            print('开始创建文件夹')
            folder_path=(self.folder_path+time.strftime("%Y%m%d%H%M%S",time.localtime()))
            self.mkdir(folder_path)  # 创建文件夹
            print('开始切换文件夹')
            os.chdir(folder_path)  # 切换路径至上面创建的文件夹
            i = 1
            for a in all_a:  # 循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
                print(a)
                img_str = a['data-src']  # a标签中完整的style字符串
                print('a标签的src内容是：', img_str)
                i = i + 1
                img_name = str(int(time.time()) + i)
                if img_str.strip():
                    print(img_str)
                    img_url_final = img_str
                    self.save_img(img_url_final, img_name)  # 调用save_img方法来保存图片

    def save_img(self, url, name):  ##保存图片
        print('开始请求图片地址，过程会有点长...')
        img = self.request(url)
        file_name = name + '.png'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name, '图片保存成功！')
        f.close()

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers)  # 像目标url地址发送get请求，返回一个response对象。有没有headers参数都可以。
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

beauty = BeautifulPicture()  # 创建类的实例
beauty.get_pic()  # 执行类中的方法
