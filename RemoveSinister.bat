del /q C:\Users\"%USERNAME%"\AppData\Roaming\svchost.exe
reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v svchost  /f
cls
echo "[*] DONE "
echo "[*] Please Restart Your System!"
pause
