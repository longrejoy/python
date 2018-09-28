import os,time
import shutil

def mymovefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print ("{} not exist!".format(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move {} -> {}".format(srcfile,dstfile))


path = "D:\\qiubai\\11\\0\\"   # 当前文件的路径
dstpath = "D:\\qiubai\\800\\"
j = 0
#time.sleep(5)
i = 0
#k = 0
for files in os.walk(path):  
    for k in range(len(files[2])):
        if (k % 50 == 0):
            i = 0
            j += 1
        mymovefile(path + str(files[2][k]),dstpath + str(j) + "\\")
    #k += 1
