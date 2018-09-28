import urllib.request
import re
import os,time
import urllib
#import random
import socket

#
socket.setdefaulttimeout(15)

#  
def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("read html error 404")
        page = urllib.request.urlopen(url)
    except socket.timeout:
        print("read html timeout")
        page = urllib.request.urlopen(url)
    try:
        html = page.read()
    except socket.timeout:
        print("read html timrout")
        html = page.read()
    return html.decode('gbk')

def getImg(html,y,sondir):
    reg = r'src="(.+?\.gif)" style="width:'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    
    x = 0


    path = 'D:\\qiubai\\gif\\02\\' + str(sondir)
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'      
    #temp = random.randint(1,1000000000)
    for imgurl in imglist:  
        try:
            urllib.request.urlretrieve(imgurl,'{}{}.gif'.format(paths,y*100+x))
            print("download picture {} success".format(x))
            x = x + 1
        except socket.timeout:
            print("download picture {} fail".format(x))
            break
        except urllib.error.URLError as e:
            print("download picture {} fail".format(x))
            break
    return imglist 

web0 = "http://www.qiubaichengnian.com/gif/list_3_"
web2 = ".html"
web = 72
x = 0
son = 0
while(1):
    web1 = web0 + str(web) + web2
    x = x + 1
    if x == 50:
        x = 0
        son += 1
    try:
        html = getHtml(web1)
    except socket.timeout:
        print("getHtml Timeout, try again")
        break

    try:
        getImg(html,x,son)
        print("download " + web1 + " success")
    except socket.timeout:
        print("GetImg Timeout")
        web1 = getNextPag(html)
        break

    web += 1

