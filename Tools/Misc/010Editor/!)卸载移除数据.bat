@ECHO OFF&(PUSHD "%~DP0")&(REG QUERY "HKU\S-1-5-19">NUL 2>&1)||(
powershell -Command "Start-Process '%~sdpnx0' -Verb RunAs"&&EXIT)

taskkill /F /IM assistant.exe >NUL 2>NUL
taskkill /F /IM 010Editor.exe >NUL 2>NUL

regsvr32 /s /u shlext010x64.dll
rd/s/q "%AppData%\Adobe\SweetScape"2>NUL
rd/s/q "%AppData%\Adobe\SweetScape-zh"2>NUL
rd/s/q "%LocalAppData%\cache\myhelp\" 2>NUL

reg delete "HKCU\Software\SweetScape" /f>NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\.1sc" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\.hex" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\.s19" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\.s28" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\.s37" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\010 Editor" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\010 Editor.bt" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\010 Editor.hex" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\010 Editor.srecords" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\Applications\010Editor.EXE" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Shell Extensions" /f  >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\*\shellex\ContextMenuHandlers\010 Editor Shell Extension" /f >NUL 2>NUL
reg delete "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /f /v "%~dp0010Editor.exe" >NUL 2>NUL
ASSOC .=. >NUL 2>NUL
ECHO.&ECHO Íê³É &TIMEOUT /t 2 >NUL&EXIT