import requests,os,time
from lxml import html
from selenium import webdriver

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115'}

### 方法 ###
# url:需要爬数据的网址 返回网站爬取的数据(静态)
def get_tree(url):
    page = requests.session().get(url, headers=headers)
   # print(page.apparent_encoding) #查看网页返回的字符集类型
   # print(page.encoding) #查看自动判断的字符集类型(生成的字符集类型)
    page.encoding='utf-8' #不同则转码
    tree = html.fromstring(page.text)
    #print(page.text) #输出网页源码
    return  tree
# url:需要爬数据的网址 返回网站爬取的数据(动态 Microsoft Edge浏览器)
def get_tree_dongtai(url):
    driver = webdriver.Edge(executable_path='msedgedriver.exe')
    driver.get(url)
    html_text = driver.page_source
    #print(html_text) #输出网页源码
    tree = html.fromstring(html_text)  # 转化为html
    driver.quit()  # 关闭浏览器
    return  tree
# 获取list的长度
def get_count(list):
    length = 0
    for list1 in list:
        count = list.count(list1)
        length = length + count
    return length
#生成文件夹和文件
def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    #拆分目录和文件
    p, f = os.path.split(path)
    print(p) #目录
    print(f) #文件名
    # 判断路径是否存在
    isExists = os.path.exists(p)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(p)

'''
#Main 小说爬虫
starturl='https://www.lingdiankanshu.co/258400/1316099.html'  # 起始章的url
src = 'E:\\爬虫\\小说\\大劫主.txt' #存放位置
mkdir(src) #没有此路径则创建 
i=0
title=[]
while i < 2500: #2500为 循环进入下一页2500次 ，根据需要自行调整
    tree1 = get_tree(starturl)
    # 下一页
    nextpage = tree1.xpath('//div[@class="section-opt m-bottom-opt"]//a[3]/text()') #爬取下一页
    nextpageurl = tree1.xpath('//div[@class="section-opt m-bottom-opt"]//a[3]/@href') #下一页的url
    if(title == tree1.xpath('//h1[@class="title"]/text()')):
        title = []
    else:
        title = tree1.xpath('//h1[@class="title"]/text()')  # 标题
    content_list = tree1.xpath('//div[@class="content"]/text()')  # 内容
    content = '\r\n'.join(title + content_list[:-1])  # 整理格式
    # 打开文件夹并且，编码设置成utf-8
    f = open(src, 'a', encoding='utf-8') # a:不覆盖 w:覆盖
    f.write(content)  # 写入章节内容
    print(content)
    a = 'https://www.lingdiankanshu.co' + nextpageurl[0]
    starturl = a
    i=i+1
f.close() #关闭文件
'''

'''
#Main 图片爬虫
imageUrl ='https://sc.chinaz.com/tupian/'
tree=get_tree(imageUrl)
image = tree.xpath('//div//a[@target="_blank"]//img/@src2') #图片路径
imageName=tree.xpath('//div//a[@target="_blank"]//img/@alt') #图片名称
imagePath=[]
for image1 in image:
    imagePath.append('https:'+image1)
#保存图片
i=0
length=get_count(imagePath)
while i<= length:
    i=i+1
    data = requests.get(imagePath[i], timeout=20).content
    f = open('E:\\爬虫\\图片\\' + imageName[i]+ '.jpg', 'wb')  # 下载图片，并保存和命名
    f.write(data)
    print(length-1-i)
f.close()
'''

'''
#视频爬虫
tree=get_tree_dongtai('http://www.pearvideo.com/video_1728429')
videourl =tree.xpath('//video/@src')
videoname =tree.xpath('//div[@id="poster"]//img/@alt')
#按照路径下载视频
try:
    r=requests.get(videourl[0])
    path="E:\\爬虫\\视频\\"+videoname[0]+".mp4"  #保存路径，后面两个冒号里，是给视频改了个名字
    f=open(path,"wb")
    f.write(r.content)
    f.close()
    print("下载完成")
except:
    print("下载失败")
'''

#歌曲爬虫
tree = get_tree_dongtai('http://www.htqyy.com/top/hot')
musicname = tree.xpath('//li[@class="mItem"]//span[@class="title"]//a/text()')
musicurl = tree.xpath('//li[@class="mItem"]//span[@class="title"]//a/@sid')
# http://f3.htqyy.com/play9/62/mp3/5 推测出62为id，该路径为地址
allurl=[]
for url1 in musicurl:
   allurl.append('http://f3.htqyy.com/play9/'+url1 +'/mp3/5')
print(allurl)
try:
    for i in range(0, len(allurl)):
        r = requests.get(allurl[0],params="",headers=headers)
        path = "E:\\爬虫\\音乐\\" + musicname[i] + ".mp3"  # 保存路径，后面两个冒号里，是给视频改了个名字
        f = open(path, "wb")
        f.write(r.content)
        #time.sleep(0.5)
        print(path + '下载完成')
    f.close()
except:
    print("下载失败")


