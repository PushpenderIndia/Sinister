sudo dpkg --add-architecture i386 && apt-get update && apt-get install wine32 python3-pip pyinstaller -y
#Downloading Required Executables
wget "https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe" 
#Installing Executables in Wine
wine /i python-3.7.4.exe
wine pywin32-227.win32-py3.7.exe
#Installing Dependencies [Python Modules] in Wine
sudo wine ~/.wine/drive_c/Python37-32/python.exe -m pip install pyinstaller pynput mss==4.0.3 essential_generators==0.9.2 six==1.12.0 python-xlib==0.25 win32gui pywin32
#Installing Dependencies in Linux 
sudo python3 -m pip install pynput
sudo python3 -m pip install mss==4.0.3
sudo python3 -m pip install essential_generators==0.9.2
sudo python3 -m pip install six==1.12.0 
sudo python3 -m pip install python-xlib==0.25
