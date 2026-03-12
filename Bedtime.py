import os
from datetime import datetime
import psutil
import winrt.windows.ui.notifications as notifications

killapps = ["discord.exe", "chrome.exe", "steam.exe"]

now = datetime.now()

if now.weekday() < 5 and now.hour == 23 and now.minute == 25:
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in apps:
            proc.kill()
        if proc.info['name'] in TerminateApps:
            proc.terminate()

    os.system("shutdown /s /t 0")