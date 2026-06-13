@echo off
title Localhost Gateway Boot Engine

start /min "" cmd /c "cd /d D:\offline\websites\osdev_wiki && python -m http.server 8080 --bind 127.0.0.1"

timeout /t 2 >nul

start "" "D:\offline\main.html"

echo started success.
timeout /t 1 >nul
exit
