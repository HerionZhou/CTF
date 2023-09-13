@ECHO OFF&(PUSHD "%~DP0")
IF NOT EXIST "%ProgramW6432%" (ECHO 此为64位版 &PING 127.1 /n 2 >NUL&EXIT)
(REG QUERY "HKU\S-1-5-19">NUL 2>&1)||(reg add "HKCU\SOFTWARE\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /f /v "%~dp0010Editor.exe" /d "~ RUNASADMIN" >NUL 2>NUL)
(REG QUERY "HKU\S-1-5-19">NUL 2>&1)||(powershell -Command "Start-Process '%~sdpnx0' -Verb RunAs" &&EXIT)

taskkill /F /IM assistant.exe >NUL 2>NUL
taskkill /F /IM 010Editor.exe >NUL 2>NUL

::注册激活信息（程序已破解）
::reg delete "HKCU\SOFTWARE\SweetScape\010 Editor\CLASSES" /f >NUL 2>NUL
reg add "HKCU\Software\SweetScape\010 Editor" /f /v "Name" /d "AnyOne" >NUL 2>NUL
reg add "HKCU\Software\SweetScape\010 Editor" /f /v "Password" /d "249F-FBAC-E9C0-A536-3055" >NUL 2>NUL

::复制汉化的后台缓存配置文件
md "%LocalAppData%\cache\myhelp"2>NUL
md "%AppData%\SweetScape-zh\010 Editor" 2>NUL
echo f|copy /y "%~dp0Data\010Editor.qhc" "%LocalAppData%\cache\myhelp\" >NUL 2>NUL
echo f|copy /y "%~dp0Data\010Editor110.cfg" "%AppData%\SweetScape-zh\010 Editor\" >NUL 2>NUL

:Menu
ECHO.
ECHO 1、关联产品文件类型
ECHO 2、添加资源管理器右键 010 Editor 项
ECHO 3、删除资源管理器右键 010 Editor 项
IF EXIST "%WinDir%\System32\CHOICE.exe" CHOICE /C 123 /N >NUL 2>NUL
IF EXIST "%WinDir%\System32\CHOICE.exe" IF "%ERRORLEVEL%"=="3" GOTO RemoveMenu
IF EXIST "%WinDir%\System32\CHOICE.exe" IF "%ERRORLEVEL%"=="2" GOTO AddMenu
IF EXIST "%WinDir%\System32\CHOICE.exe" IF "%ERRORLEVEL%"=="1" GOTO Assoc
IF NOT EXIST "%WinDir%\System32\CHOICE.exe" ECHO.&SET /p choice=输入选项数字敲回车键：
IF NOT EXIST "%WinDir%\System32\CHOICE.exe" IF NOT "%choice%"=="" SET choice=%choice:~0,1%
IF NOT EXIST "%WinDir%\System32\CHOICE.exe" IF /I "%choice%"=="1" GOTO Assoc
IF NOT EXIST "%WinDir%\System32\CHOICE.exe" IF /I "%choice%"=="2" GOTO AddMenu
IF NOT EXIST "%WinDir%\System32\CHOICE.exe" IF /I "%choice%"=="3" GOTO RemoveMenu
IF NOT EXIST "%WinDir%\System32\CHOICE.exe" ECHO.&ECHO 输入无效 &PAUSE&CLS&GOTO MENU

:Assoc
reg add "HKLM\SOFTWARE\Classes\.1sc" /f /ve /d "010 Editor.1sc" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\.bt" /f /ve /d "010 Editor.bt" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\.hex" /f /ve /d "010 Editor.hex" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\.s19" /f /ve /d "010 Editor.srecords" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\.s28" /f /ve /d "010 Editor.srecords" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\.s37" /f /ve /d "010 Editor.srecords" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor" /f /ve /d "010 Editor" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor\DefaultIcon" /f /ve /d "\"%~dp0010Editor.EXE\",2" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor\shell\open\command" /f /ve /d "\"%~dp0010Editor.EXE\" \"%%1\"" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.1sc" /f /ve /d "010 Editor Script File" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.1sc\DefaultIcon" /f /ve /d "\"%~dp0010Editor.EXE\",3" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.1sc\shell\open\command" /f /ve /d "\"%~dp0010Editor.EXE\" \"-script:%%1@1\"" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.bt" /f /ve /d "010 Editor Binary Template" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.bt\DefaultIcon" /f /ve /d "\"%~dp0010Editor.EXE\",4" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.bt\shell\open\command" /f /ve /d "\"%~dp0010Editor.EXE\" \"-template:%%1@1\"" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.hex" /f /ve /d "Intel Hex File" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.hex\DefaultIcon" /f /ve /d "\"%~dp0010Editor.EXE\",2" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.hex\shell\open\command" /f /ve /d "\"%~dp0010Editor.EXE\" -import:\"%%1\"" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.srecords" /f /ve /d "Motorola S-Records" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.srecords\DefaultIcon" /f /ve /d "\"%~dp0010Editor.EXE\",2" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\010 Editor.srecords\shell\open\command" /f /ve /d "\"%~dp0010Editor.EXE\" -import:\"%%1\"" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Classes\Applications\010Editor.EXE\shell\open\command" /f /ve /d "\"%~dp0010Editor.EXE\" \"%%1\"" >NUL 2>NUL
ASSOC .=. >NUL 2>NUL
IF EXIST "%WinDir%\System32\CHOICE.exe" ( 
ECHO.&ECHO 关联完成 &TIMEOUT /t 2 >NUL & CLS & GOTO MENU
) ELSE ( 
ECHO.&ECHO 关联完成，任意键返回 &PAUSE>NUL&CLS&GOTO MENU) 

:AddMenu
regsvr32 /s shlext010x64.dll
reg add "HKLM\SOFTWARE\Classes\*\shellex\ContextMenuHandlers\010 Editor Shell Extension" /f /ve /d "{792252D0-144F-11E1-BE50-0800200C9A66}" >NUL 2>NUL
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Shell Extensions\Approved" /f /v "{792252D0-144F-11E1-BE50-0800200C9A66}" /d "010 Editor Shell Extension" >NUL 2>NUL
IF EXIST "%WinDir%\System32\CHOICE.exe" ( 
ECHO.&ECHO 添加完成 &TIMEOUT /t 2 >NUL & CLS & GOTO MENU
) ELSE ( 
ECHO.&ECHO 添加完成，任意键返回 &PAUSE>NUL&CLS&GOTO MENU) 

:RemoveMenu
regsvr32 /s /u shlext010x64.dll
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Shell Extensions" /f >NUL 2>NUL
reg delete "HKLM\SOFTWARE\Classes\*\shellex\ContextMenuHandlers\010 Editor Shell Extension" /f >NUL 2>NUL
IF EXIST "%WinDir%\System32\CHOICE.exe" ( 
ECHO.&ECHO 删除完成 &TIMEOUT /t 2 >NUL & CLS & GOTO MENU
) ELSE ( 
ECHO.&ECHO 删除完成，任意键返回 &PAUSE>NUL&CLS&GOTO MENU) 