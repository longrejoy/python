import os
path = 'D:\\movie\\fcw62\\'
count = 1
for file in os.listdir(path):
    os.rename(os.path.join(path,file),os.path.join(path,'mp4'+str(count)+".mp4"))
    count+=1
