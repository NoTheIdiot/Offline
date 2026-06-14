@echo off
setlocal enabledelayedexpansion
cls

set count=0
for %%f in (*.mp4) do (
    set /a count+=1
    set "video[!count!]=%%f"
    <nul set /p="[!count!] %%f"
    cd.
)

if %count%==0 exit

set /p choice=""

if not defined video[%choice%] exit

start "" "!video[%choice%]!"
