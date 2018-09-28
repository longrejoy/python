import urllib.request
import re
import os,time
import urllib
from urllib.parse import quote
import  string
import random

str0 = "http://newoss.maiziedu.com/matplotlib/matplotlib"

#i = 1
str2 = ".mp4"
path = 'D:\\maiziedu\\visual'
if not os.path.isdir(path):  
    os.makedirs(path)
for j in range(1,34):
    web = str0 + str(j) + str2
    urllib.request.urlretrieve(quote(web, safe = string.printable),'{}{}.mp4'.format(path,j))
    print("download {} success".format(web))


