import os
from datetime import datetime
import psutil
import winrt.windows.ui.notifications as notifications

apps = ["discord.exe", "chrome.exe", "steam.exe"]

now = datetime.now()

if now.weekday() < 5 and now.hour == 23 and now.minute == 25:
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in apps:
            proc.kill()

    os.system("shutdown /s /t 0")