from pymouse import PyMouse
from pykeyboard import PyKeyboard
import requests,time,threading,ctypes
from pynput import keyboard
import sys
import pyperclip

flag=False
play=True
pause=False

mode=int(input("选择模式：1.键盘复制 2.鼠标复制 3.鼠标复制(不带全选)"))
if(mode!=1 and mode!=2 and mode!=3):
    input("没有这个选项")
    sys.exit()

def worker1():
    global play
    global pause
    global flag
    def on_press(key):
        global play
        global pause
        global flag
        # whnd = ctypes.windll.kernel32.GetConsoleWindow()
        # if(str(key)=='Key.ctrl_l'):    
        #     ctypes.windll.user32.ShowWindow(whnd, 0)
        # if(str(key)=='Key.ctrl_r'):
        #     ctypes.windll.user32.ShowWindow(whnd, 1)
        if(str(key)=='Key.f9'):
            print("-----------------------------------启动-----------------------------------")
            play=True
            pause=False
        if(str(key)=='Key.f10'):
            print("-----------------------------------暂停-----------------------------------")
            play=False
            pause=True
        if(str(key)=='Key.ctrl_l'):
            flag=True
            #print(flag)
        #print(str(key))
        
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def worker2():
    global play
    global pause
    global flag
    m = PyMouse()
    k = PyKeyboard()
    print("鼠标移动到软件1文本框 按 ctrl")
    flag=False
    while(1):
        #print(flag)
        if(flag==True):
            a = m.position()    #获取当前坐标的位置
            print(a)
            flag=False
            break
        
    if(mode==2 or mode==3):
        print("鼠标移动到 复制 按 ctrl")
        while(1):
            if(flag==True):
                d = m.position()    #获取当前坐标的位置
                print(d)
                flag=False
                break

    print("鼠标移动到软件2文本框 按 ctrl")
    while(1):
        if(flag==True):
            b = m.position()    #获取当前坐标的位置
            print(b)
            flag=False
            break
    
    print("鼠标移动到 发送 按 ctrl")
    while(1):
        if(flag==True):
            c = m.position()    #获取当前坐标的位置
            print(c)
            flag=False
            break

    

    ti1=float(input("输入检测延时："))
    ti=float(input("输入发送延时："))
    s=''
    while(1):
        time.sleep(ti1)
        if(play==True):
            m.click(a[0],a[1])  #移动并且在(x,y)位置左击

            if(mode!=3):
                k.press_key(k.control_l_key) #全选
                k.tap_key('a')
                k.release_key(k.control_l_key)
            
            if(mode==1):
                #键盘复制
                k.press_key(k.control_l_key) 
                k.tap_key('c')
                k.release_key(k.control_l_key)
            
            if(mode==2 or mode==3):
                #鼠标复制
                m.click(a[0]-5,a[1],2)
                time.sleep(1)
                m.click(d[0]-5,d[1])
            
            time.sleep(1)
            
            if(pyperclip.paste()!=s):
                #转发
                print("延迟%s秒"%ti)
                time.sleep(ti)
                s=pyperclip.paste()
                m.click(b[0],b[1])
                k.press_key(k.control_l_key) #粘贴
                k.tap_key('v')
                k.release_key(k.control_l_key)
                time.sleep(0.5)
                m.click(c[0],c[1])           #发送
            if(play==False):
                while(1):
                    if(play==True):
                        break


def Beijing_time():
    r=requests.get('https://www.baidu.com')
    t=time.strptime(r.headers['date'],'%a, %d %b %Y %H:%M:%S GMT')
    return time.mktime(t)+28800

if __name__ == '__main__':
    # if(Beijing_time() - 1582788049 > 86400*3 ):
    #     input("测试期已过。")
    #     sys.exit()
    
    t1 =threading.Thread(target=worker1)
    t1.start()   
    t2 =threading.Thread(target=worker2)
    t2.start()
