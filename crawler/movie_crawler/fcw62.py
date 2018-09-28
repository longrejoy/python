import urllib.request
import re
import os,time
import urllib
from urllib.parse import quote
import  string
import random
def getHtml(url):
    try:
        page = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print("read html error 404")
        return 0
    html = page.read()
    return html.decode('UTF-8')

def getImg(html,y,sondir):
    reg = r'href="(.+?\.mp4)" data'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    
    x = 0

    #path = 'D:\\96il_new'  
    #if (y == 10):
    path = 'D:\\fcw62_new\\' + str(sondir)
    if not os.path.isdir(path):  
        os.makedirs(path)  
    paths = path+'\\'
    #print(imglist)      
    #temp = random.randint(1,1000000000)
    for imgurl in imglist:  
        try:
            urllib.request.urlretrieve(quote(imgurl, safe = string.printable),'{}{}.mp4'.format(paths,y*100+x))
            print("download video {} success".format(x))
            x = x + 1
    #    except socket.timeout:
    #        print("download picture {} fail".format(x))
    #        break
        except urllib.error.URLError as e:
            print("download video {} fail".format(x))
            break
    return imglist 

def getNextPag(html):
    reg1 = r'target="_blank" href="(.+?)" title="'
    webre = re.compile(reg1)
    weblist = webre.findall(html)
    return weblist

web1 = "https://www.fcw62.com/videos/4420/82/"
x = 9
son = 0
while(1):
    x = x + 1
    if x == 35:
        x = 10
        son += 1
    j = 1
    html = getHtml((web1))
    while (html == 0):
        html = getHtml((list_r[j]))
        j += 1
    #except socket.timeout:
    #    print("getHtml Timeout, try again")
    #    break

    #try:
    getImg(html,x,son)
    print("download " + web1 + " success")
    #except socket.timeout:
    #    print("GetImg Timeout")
    #    web1 = getNextPag(html)
    #    break

    #try:
    list_r = getNextPag(html)
    web1 = list_r[random.randint(0,11)]
    print("get next page success!")
    print("Next page:{}".format(web1))
    web1 = quote(web1, safe = string.printable)
    #except socket.timeout:
    #    print("getNextPag Timeout, try again")
    #    break
