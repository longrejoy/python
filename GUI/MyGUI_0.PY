import os
from time import sleep
from tkinter import *
#import tkinter

def main():
    top = Tk()

    top.wm_title('MyGUI')#设置窗体标题
    
    top.wm_minsize(400, 400)#设置窗口最小化大小
    top.wm_maxsize(2800, 2800)#设置窗口最大化大小
    top.resizable(width=0, height=0)#设置窗口宽度不可变，高度可变


    #label1 = tkinter.Label(top,text='Directory Lister')
    #label1.pack()

    #frame1 = tkinter.Frame(top,height = 512, width = 512)
    #frame1.pack()
    
    #scrollbar1 = tkinter.Scrollbar(frame1)
    #scrollbar1.pack(side='right',expand=1,in_= frame1, fill= 'both',ipadx=48,ipady=48)
    
    #entry1 = tkinter.Entry(frame1)
    #entry1.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    #listbox1 = tkinter.Listbox(frame1)
    #listbox1.pack(side='left',expand=1,fill='both',ipadx=48,ipady=48)

    #bottom1 = tkinter.Button(frame1,text='previous page')
    #bottom1.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    #bottom2 = tkinter.Button(frame1,text='next page')
    #bottom2.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    canvas1 = Canvas(top,bg='blue',width=666,height=666)
    canvas1.pack(side='bottom')

    #3、创建一个items,坐标为(10,10,110,110)，并填充颜色为红色
    #canvas1.create_rectangle(0,0,100,100,fill = 'white',outline= 'black',width=15)
    
    #4、指定矩形的边框颜色为绿色
    canvas1.create_rectangle(3,3,257,257,fill = 'white',outline = 'white',width=0)
    
    #5、指定边框的宽度
    #canvas1.create_rectangle(230,10,330,110,outline = 'black',width = 20)
    
    #6、画虚线
    # 使用属性dash,这个值只能为奇数
    #canvas1.create_rectangle(0,100,100,200,outline = 'black',width = 10,dash = 3)
    
    #7、使用画刷填充
    # 使用属性stipple
    #canvas1.create_rectangle(100,100,200,200,fill = 'red',outline = 'black',width = 10,dash = 3,stipple = 'gray12')
    
    #8、修改item的坐标
    # 使用Canvas的方法coords(原item,坐标元组)来重新设置item的坐标
    # 重新设置rt的坐标（相当于移动一个item）
    #rt = canvas1.create_rectangle(570,10,660,110,fill = 'green',outline = 'black',width = 5,dash = 7,stipple = 'gray12')
    #canvas1.coords(rt,(680,10,770,110))

    #checkbutton1 = tkinter.Checkbutton(frame1)
    #checkbutton1.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    #menubutton1 = tkinter.Menubutton(frame1)
    #menubutton1.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    #menu1 = tkinter.Menu(frame1)
    #menu1.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    #message1 = tkinter.Message(frame1)
    #message1.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    #radiobutton = tkinter.Radiobutton(frame1)
    #radiobutton.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    #scale1 = tkinter.Scale(frame1)
    #scale1.pack(expand=1,side='bottom',fill='both',ipadx=48,ipady=48)

    top.mainloop()

    #mainloop()

if __name__ == '__main__':
    main()