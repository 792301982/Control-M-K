from pymouse import PyMouse
from pykeyboard import PyKeyboard
import requests,time,threading,ctypes
from pynput import keyboard
from pynput.keyboard import Key
import sys
import pyperclip

flag=False
play=True
pause=False

m = PyMouse()
positions=list()

def worker1():
    global play
    global pause
    global flag
    def on_press(key):
        global play
        global pause
        global flag
        #print(str(key))
        if(str(key)=='Key.ctrl_l'):
            flag=True
        keys=['<97>','<98>','<99>','<100>','<101>','<102>','<103>','<104>','<105>']
        for i in keys:
            try:
                if(str(key)==i):
                    ind=keys.index(i)
                    m.click(positions[ind][0],positions[ind][1])  #移动并且在(x,y)位置左击
            except:
                return

        
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def worker2():
    global play
    global pause
    global flag
    
    for i in range(1,10):
        print("鼠标移动到位置"+str(i)+"按 ctrl")
        flag=False
        while(1):
            if(flag==True):
                a = m.position()    #获取当前坐标的位置
                print(a)
                positions.append(a)
                flag=False
                break
    print("按%s进行操作" % str('小键盘'))

        
def Beijing_time():
    r=requests.get('https://www.baidu.com')
    t=time.strptime(r.headers['date'],'%a, %d %b %Y %H:%M:%S GMT')
    return time.mktime(t)+28800

if __name__ == '__main__':
    # if(Beijing_time() - 1584598695 > 86400*1 ):
    #     input("测试期已过。")
    #     sys.exit()
    
    t1 =threading.Thread(target=worker1)
    t1.start()   
    t2 =threading.Thread(target=worker2)
    t2.start()
