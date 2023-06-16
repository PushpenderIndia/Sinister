import subprocess
from urllib.request import urlopen
import banners
import time

def update_client_version(version):
    with open("version.txt", "r") as vnum:
        if vnum.read() != version:
            return True
        else:
            return False

def main():
    try:
        version = urlopen("https://raw.githubusercontent.com/PushpenderIndia/Sinister/master/version.txt").read()
    except Exception as e:
        print("[!] Unable to Fetch Origin version.txt")
        print("[!] Please Check Your Internet Connection!")
        print("[*] Exiting ...")
        quit()
        
    if update_client_version(version) is True:
        subprocess.call(["git", "pull", "origin", "master"])
        return "[+] Updated to latest version: v{}..".format(version)
    else:
        return "[*] You are already up to date with git origin master :)"


if __name__ == '__main__':
    print(banners.get_banner())
    print("\t\tAuthor: Pushpender | Github: github.com/PushpenderIndia\n")
    print("[*] Welcome to Sinister's Auto Updater")
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print("[*] Please Note : Git must be installed in order to use \"updater.py\"")
    time.sleep(5)
    print("[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]")
    print("[*] Checking Sinister's version information..")
    print(main())
    print("[*] Exiting ...")
