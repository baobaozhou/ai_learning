#爬取微博评论
# import requests
# import re
# base_url='https://m.weibo.cn/comments/hotflow?id=4266483972261566&mid=4266483972261566&max_id='
# url=['146937897333819']
# n=0
# while n<100:
#     rea_url=base_url+url[n]
#     html=requests.get(rea_url)
#     page=str(html.json()['data']['max_id'])
#     url.append(page)
#     for m in range(len(html.json()['data']['data'])):
#         data=html.json()['data']['data'][m]['text']
#         res=''.join(re.findall(r'[\u4e00-\u9fa5]',data))
#         with open('C:\\Users\\墨宝宝大撒比\\Desktop\\1.txt','a')as f:
#             f.write(res+'\n')
#     n=n+1

# #爬取图片
# import os
# import re
# import urllib.request
# # 打开网址，获取网址信息
# def openUrl(url):
#         req = urllib.request.Request(url)
#         # 添加 header 信息
#         # req.add_header{
#         #     'User-Agent'
#         #     'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
#         # }
#         response = urllib.request.urlopen(req)
#         html = response.read()
#         return html
# # 用正则表达式，找到图片链路
# def findImgs(url):
#         html = openUrl(url).decode('utf-8')    # 解码
#         # 编写正则表达式
#         informations = r'"objURL":"(.*?)"'
#         # 返回一个正则表达式对象
#         reg = re.compile(informations, re.S)
#         # 开始查找所有信息
#         contents_list = re.findall(reg, html)
#         contents = []
#         for content in contents_list:
#                 contents.append(content)
#         return contents
# # 下载图片folder为文件夹位置，img_addrs存储着图片的链路地址
# def saveImgs(folder, img_addrs):
#         for each in img_addrs:
#                 print(each)
#                 filename = each.split('/')[-1]
#                 with open(filename, 'wb') as f:
#                         img = openUrl(each)
#                         f.write(img)
# def download(folder='E:\\bizhi'):
#         os.chdir(folder)
#         url = 'http://image.baidu.com/search/index?ct=201326592&tn=baiduimage&word=%E5%A3%81%E7%BA%B8%20%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC%20%E7%BE%8E%E5%A5%B3'
#         img_addrs = findImgs(url)
#         saveImgs(folder, img_addrs)
#
# if __name__ == '__main__':
#         download()

#爬取京东评论
import urllib.request
import json
import time
import random
def crawlProductComment(url,page):
    #读取原始数据(注意选择gbk编码方式)
    html = urllib.request.urlopen(url).read().decode('gbk')
    #从原始数据中提取出JSON格式数据(分别以'{'和'}'作为开始和结束标志)
    jsondata = html[27:-2]
    #print(jsondata)
    data = json.loads(jsondata)
    #print(data['comments'])
    #print(data['comments'][0]['content'])
    #遍历商品评论列表
    for i in data['comments']:
        productName = i['referenceName']
        commentTime = i['creationTime']
        content = i['content']
        #输出商品评论关键信息
        with open('C:\\Users\\墨宝宝大撒比\\Desktop\\1.txt', 'a')as f:
                f.write("用户评论内容:{}".format(content)+'\n')
        # print("商品全名:{}".format(productName))
        # print("用户评论内容:{}".format(content))

for i in range(500,700):
    print("正在获取第{}页评论数据!".format(i+1))
    #小米6评论链接,通过更改page参数的值来循环读取多页评论信息
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv15238&productId=6949475&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&fold=1'
    crawlProductComment(url,i)
    #设置休眠时间
    time.sleep(random.randint(31,33))