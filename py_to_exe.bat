@echo off
setlocal enableextensions enabledelayedexpansion
call :getargc argc %*
if %argc% NEQ 1 (
        echo "Error: must have 1 argument"
        exit
)
set filename=%1
if not exist %filename% (
        echo "Error: %filename% not found"
        exit
)

pyinstaller --onefile %filename%
del %filename:~0, -3%.spec
move .\dist\%filename:~0, -3%.exe ./
rmdir dist
rmdir .\build\ /s /q


endlocal
goto :eof

:getargc
    set getargc_v0=%1
    set /a "%getargc_v0% = 0"
:getargc_l0
    if not x%2x==xx (
        shift
        set /a "%getargc_v0% = %getargc_v0% + 1"
        goto :getargc_l0
    )
    set getargc_v0=
    goto :eof