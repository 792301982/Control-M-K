from pymouse import PyMouse
from pykeyboard import PyKeyboard
import requests,time,threading,ctypes
from pynput import keyboard
from pynput.keyboard import Key
import sys
import pyperclip

flag=False
flag_a=False
play=True
pause=False

m = PyMouse()
positions=list()

sleep_time=input("设置两次点击间隔时间：")
def worker1():
    global play
    global pause
    global flag
    global flag_a

    def on_press(key):
        global play
        global pause
        global flag
        global flag_a
        #print(str(key))
        if(str(key)=='Key.ctrl_l'):
            flag=True
        if(str(key)=='Key.f2'):
            flag_a=True
        if(str(key)=='Key.f3'):
            flag_a=False


        
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def worker2():
    global play
    global pause
    global flag
    global flag_a
    
    for i in range(1,3):
        print("鼠标移动到位置"+str(i)+"按 ctrl")
        flag=False
        while(1):
            if(flag==True):
                a = m.position()    #获取当前坐标的位置
                print(a)
                positions.append(a)
                flag=False
                break
    print("按%s开始，%s关闭" % (str('f2'),'f3'))
    while(1):
        if(flag_a==True):
            m.click(positions[0][0],positions[0][1])  #移动并且在(x,y)位置左击
            time.sleep(float(sleep_time))
            m.click(positions[1][0],positions[1][1])  #移动并且在(x,y)位置左击
            time.sleep(float(sleep_time))
        else:
            pass

        
def Beijing_time():
    r=requests.get('https://www.baidu.com')
    t=time.strptime(r.headers['date'],'%a, %d %b %Y %H:%M:%S GMT')
    return time.mktime(t)+28800

if __name__ == '__main__':
    # if(Beijing_time() - 1594897362 > 86400*1 ):
    #     input("测试期已过。")
    #     sys.exit()
    
    t1 =threading.Thread(target=worker1)
    t1.start()   
    t2 =threading.Thread(target=worker2)
    t2.start()
