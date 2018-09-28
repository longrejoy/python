from Ui_2048 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow
import random
from PyQt5.QtWidgets import QMessageBox

h_list=[[0,0,0,0],[0,0,0,0],[2,0,0,0],[4,2,0,0]]
#h_list=[[0,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
score = 0
def NewNumber(widget):
    count = 0
    for i in range(4):
        for j in range(4):
            if h_list[i][j] == 2048:
                print('win')
                My_Message = QMessageBox.about(widget.centralwidget,'Win','Win')
            if h_list[i][j]:
                count += 1
    if count == 16:
        print('fail')
        My_Message = QMessageBox.about(widget.centralwidget,'Fail','Fail')
    else:
        x = random.randint(0,3)
        y = random.randint(0,3)
        while (h_list[x][y]):
            x = random.randint(0,3)
            y = random.randint(0,3)
        h_list[x][y] = 2
        print('new')
        for i in range(4):
            z=''
            for j in range(4):
                z=z + str(h_list[i][j])+' '
            print(z)
        Remap(widget)

def Left():
    global score
    for k in range(3):
        for i in range(4):
            for j in range(3):
                if (not h_list[i][j]):
                    temp = h_list[i][j]
                    h_list[i][j] = h_list[i][j+1]
                    h_list[i][j+1] = temp
    for i in range(4):
        for j in range(3):
            if h_list[i][j] == h_list[i][j+1]:
                h_list[i][j] = h_list[i][j] + h_list[i][j+1]
                score = score + h_list[i][j+1]
                h_list[i][j+1] = 0
                break
    for k in range(3):
        for i in range(4):
            for j in range(3):
                if (not h_list[i][j]):
                    temp = h_list[i][j]
                    h_list[i][j] = h_list[i][j+1]
                    h_list[i][j+1] = temp
    print('after')
    for i in range(4):
        z=''
        for j in range(4):
            z=z + str(h_list[i][j])+' '
        print(z)        
    return 0

def Right():
    global score
    for k in range(3):
        for i in range(4):
            for j in range(3):
                if (not h_list[3-i][3-j]):
                    temp = h_list[3-i][3-j]
                    h_list[3-i][3-j] = h_list[3-i][2-j]
                    h_list[3-i][2-j] = temp
    for i in range(4):
        for j in range(3):
            if h_list[3-i][3-j] == h_list[3-i][2-j]:
                h_list[3-i][3-j] = h_list[3-i][3-j] + h_list[3-i][2-j]
                score = score + h_list[3-i][2-j]
                h_list[3-i][2-j] = 0
                break
    for k in range(3):
        for i in range(4):
            for j in range(3):
                if (not h_list[3-i][3-j]):
                    temp = h_list[3-i][3-j]
                    h_list[3-i][3-j] = h_list[3-i][2-j]
                    h_list[3-i][2-j] = temp
    print('after')
    for i in range(4):
        z=''
        for j in range(4):
            z=z + str(h_list[i][j])+' '
        print(z)
    return 0

def Up():
    global score
    for k in range(3):
        for j in range(4):
            for i in range(3):
                if (not h_list[i][j]):
                    temp = h_list[i][j]
                    h_list[i][j] = h_list[i+1][j]
                    h_list[i+1][j] = temp
    for j in range(4):
        for i in range(3):
            if (h_list[i][j] == h_list[i+1][j]):
                h_list[i][j] = h_list[i][j] + h_list[i+1][j]
                score = score + h_list[i+1][j]
                h_list[i+1][j] = 0
                break
    for k in range(3):
        for j in range(4):
            for i in range(3):
                if (not h_list[i][j]):
                    temp = h_list[i][j]
                    h_list[i][j] = h_list[i+1][j]
                    h_list[i+1][j] = temp    
    print('after')
    for i in range(4):
        z=''
        for j in range(4):
            z=z + str(h_list[i][j])+' '
        print(z)   
    return 0

def Down():
    global score
    for k in range(3):
        for j in range(4):
            for i in range(3):
                if (not h_list[3-i][3-j]):
                    temp = h_list[3-i][3-j]
                    h_list[3-i][3-j] = h_list[2-i][3-j]
                    h_list[2-i][3-j] = temp
    for j in range(4):
            for i in range(3):
                if (h_list[3-i][3-j] == h_list[2-i][3-j]):
                    h_list[3-i][3-j] = h_list[3-i][3-j] + h_list[2-i][3-j]
                    score = score + h_list[2-i][3-j]
                    h_list[2-i][3-j] = 0
                    break
    for k in range(3):
        for j in range(4):
            for i in range(3):
                if (not h_list[3-i][3-j]):
                    temp = h_list[3-i][3-j]
                    h_list[3-i][3-j] = h_list[2-i][3-j]
                    h_list[2-i][3-j] = temp
    print('after')
    for i in range(4):
        z=''
        for j in range(4):
            z=z + str(h_list[i][j])+' '
        print(z)   
    
    return 0

class MainWindow_2048(Ui_MainWindow,QMainWindow):
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton_L.clicked.connect(self.On_pushButton_L_Clicked)
        self.pushButton_R.clicked.connect(self.On_pushButton_R_Clicked)
        self.pushButton_U.clicked.connect(self.On_pushButton_U_Clicked)
        self.pushButton_D.clicked.connect(self.On_pushButton_D_Clicked)
    
    def On_pushButton_L_Clicked(self):
        print('L')
        Left()
        NewNumber(self)

    def On_pushButton_R_Clicked(self):
        print('R')
        Right()
        NewNumber(self)

    def On_pushButton_U_Clicked(self):
        print('U')
        Up()
        NewNumber(self)
    
    def On_pushButton_D_Clicked(self):
        print('D')
        Down()
        NewNumber(self)

def Remap(widget):
    for i in range(4):
        for j in range(4):
            #print(i,' ',j)
            if (i == 0) and (j == 0):
                #print('0')
                if h_list[0][0]:
                    dec2str = str(h_list[0][0])
                else:
                    dec2str = ''
                widget.label_1.setText(dec2str)
            elif (i == 0) and (j == 1):
                #print('1')
                if h_list[1][0]:
                    dec2str = str(h_list[1][0])
                else:
                    dec2str = ''
                widget.label_2.setText(dec2str)
            elif (i == 0) and (j == 2):
                #print('2')
                if h_list[2][0]:
                    dec2str = str(h_list[2][0])
                else:
                    dec2str = ''
                widget.label_3.setText(dec2str)
            elif (i == 0) and (j == 3):
                #print('3')
                if h_list[3][0]:
                    dec2str = str(h_list[3][0])
                else:
                    dec2str = ''
                widget.label_4.setText(dec2str)
            elif (i == 1) and (j == 0):
                #print('4')
                if h_list[0][1]:
                    dec2str = str(h_list[0][1])
                else:
                    dec2str = ''
                widget.label_5.setText(dec2str)
            elif (i == 1) and (j == 1):
                #print('5')
                if h_list[1][1]:
                    dec2str = str(h_list[1][1])
                else:
                    dec2str = ''
                widget.label_6.setText(dec2str)
            elif (i == 1) and (j == 2):
                #print('6')
                if h_list[2][1]:
                    dec2str = str(h_list[2][1])
                else:
                    dec2str = ''
                widget.label_7.setText(dec2str)
            elif (i == 1) and (j == 3):
                #print('7')
                if h_list[3][1]:
                    dec2str = str(h_list[3][1])
                else:
                    dec2str = ''
                widget.label_8.setText(dec2str)
            elif (i == 2) and (j == 0):
                #print('8')
                if h_list[0][2]:
                    dec2str = str(h_list[0][2])
                else:
                    dec2str = ''
                widget.label_9.setText(dec2str)
            elif (i == 2) and (j == 1):
                #print('9')
                if h_list[1][2]:
                    dec2str = str(h_list[1][2])
                else:
                    dec2str = ''
                widget.label_10.setText(dec2str)
            elif (i == 2) and (j == 2):
                #print('10')
                if h_list[2][2]:
                    dec2str = str(h_list[2][2])
                else:
                    dec2str = ''
                widget.label_11.setText(dec2str)
            elif (i == 2) and (j == 3):
                #print('11')
                if h_list[3][2]:
                    dec2str = str(h_list[3][2])
                else:
                    dec2str = ''
                widget.label_12.setText(dec2str)
            elif (i == 3) and (j == 0):
                #print('12')
                if h_list[0][3]:
                    dec2str = str(h_list[0][3])
                else:
                    dec2str = ''
                widget.label_13.setText(dec2str)
            elif (i == 3) and (j == 1):
                #print('13')
                if h_list[1][3]:
                    dec2str = str(h_list[1][3])
                else:
                    dec2str = ''
                widget.label_14.setText(dec2str)
            elif (i == 3) and (j == 2):
                #print('14')
                if h_list[2][3]:
                    dec2str = str(h_list[2][3])
                else:
                    dec2str = ''
                widget.label_15.setText(dec2str)
            elif (i == 3) and (j == 3):
                #print('15')
                if h_list[3][3]:
                    dec2str = str(h_list[3][3])
                else:
                    dec2str = ''
                widget.label_16.setText(dec2str)
    widget.textBrowser.clear()
    widget.textBrowser.append(str(score))
    
def Initial(ui):
    Remap(ui)
    NewNumber(ui)

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=MainWindow_2048()
    widget.show()
    Initial(widget)  
    #while (1):
    #    Remap(widget)     
    sys.exit(app.exec_())

