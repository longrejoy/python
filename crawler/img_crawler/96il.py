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
    return html.decode('UTF-8')

def getImg(html,y,sondir):
    reg = r'src="(.+?\.jpg)" border='
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    
    x = 0

    #path = 'D:\\96il_new'  
    #if (y == 10):
    path = 'D:\\96il_new\\' + str(sondir)
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'      
    #temp = random.randint(1,1000000000)
    for imgurl in imglist:  
        try:
            urllib.request.urlretrieve(imgurl,'{}{}.jpg'.format(paths,y*100+x))
            print("download picture {} success".format(x))
            x = x + 1
        except socket.timeout:
            print("download picture {} fail".format(x))
            break
        except urllib.error.URLError as e:
            print("download picture {} fail".format(x))
            break
    return imglist 

def getNextPag(html):
    reg1 = r'下一页:<a href=(.+?\.html)>'
    webre = re.compile(reg1)
    weblist = webre.findall(html)
    return "http://www.96il.com" + weblist[0]

web1 = "http://www.96il.com/htm/2018/1/2/p01/395084.html"
x = 9
son = 0
while(1):
    x = x + 1
    if x == 35:
        x = 10
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

    try:
        web1 = getNextPag(html)
        print("get next page success!")
        print("Next page:{}".format(web1))
    except socket.timeout:
        print("getNextPag Timeout, try again")
        break
