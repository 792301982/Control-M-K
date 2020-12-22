from pynput import keyboard

def on_press(key):
    print(key)
    return False

def on_click(x,y,button,pressed):
    print(x,y,pressed)
    print(button)
    
with keyboard.Listener(on_press=on_press,on_click=on_click) as listener:
    listener.join()
