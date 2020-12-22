from tkinter import *
import pyperclip
import threading
from pynput import keyboard
from pynput.keyboard import Key,Controller

def on_press(key):
        global data
        global lb
        global s_l,l
        key=str(key)
        #print(key)
        if(key=='Key.f2'):
                s_l=lb.curselection()
                data=l[s_l[0]]
                paste(data[0])
        if(key=='Key.f10'):
                s_l=lb.curselection()
                data=l[s_l[0]]
                paste(data[1])
        if(key=='Key.f3'):
                s_l=lb.curselection()
                data=l[s_l[0]]
                paste(data[2])
        if(key=='Key.f12'):
                lb.select_clear(s_l[0])
                s_l=lb.curselection()
                data=l[s_l[0]]
                #s_l=lb.curselection()
                #data=l[s_l[0]]
                #paste(data[3])
        #if(key=='Key.f5'):
                #lb.select_clear(s_l[0])
                #s_l=lb.curselection()
                #data=l[s_l[0]]
                
def input_data():
	a_l=list()
	with open('1.txt',encoding='UTF-8') as f:
		for s in f:
			l=s.strip().split("----")
			a_l.append(l)
	return a_l

def paste(d):
        keyboard=Controller()
        pyperclip.copy(str(d))
        with keyboard.pressed(Key.ctrl):
                keyboard.press('v')
                keyboard.release('v')

def thread1():
        global data
        global lb
        global s_l,l
        root=Tk()
        root.title("复制粘贴 qq：792301982")
        root.geometry('400x400')
        #l=StringVar()#与变量绑定 l.set(('1','2'))
        lb=Listbox(root,selectmode=MULTIPLE,width='400',height='20')
        #MULTIPLE：多选 BROWSE：通过鼠标的移动选择 EXTENDED：shift和ctrl配合使用
        lb.pack()
        l=input_data()
        for i in l:
            lb.insert(END,i)
        lb.select_set(0,len(l))
        #lb.select_clear(4)
        t=Label(root,text="f9-f11粘贴数据  f12删除选中的第一行\n如有问题请联系本人qq 792301982")
        t.pack(side=BOTTOM)
        #s_l=lb.curselection()#返回选中项索引
        #data=l[s_l[0]]
        root.mainloop()
        
def thread2():
        #监听键盘按键
        with keyboard.Listener(on_press=on_press) as listener:
                listener.join()
        
if __name__ =="__main__":
        lock=threading.Lock()
        t1 = threading.Thread(target=thread1)
        t1.setDaemon(True)
        t1.start()
        t2=threading.Thread(target=thread2)
        t2.start()
