import os
from datetime import datetime
import time
import psutil
from win11toast import toast
kill_apps = ["Update.exe", "chrome.exe", "steam.exe"]
terminate_apps = ["Ableton Live 12 Suite.exe"]

def shutdown():
    os.system("shutdown /s /t 0")

def close_apps():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in kill_apps:
            proc.kill()
        elif proc.info['name'] in terminate_apps:
            proc.terminate()    


def week_day_shutoff():
    while True:
        now = datetime.now()
        time.sleep(360)
        print("Checking time.")
        if (now.hour == 00 and now.weekday() == 1) or (now.weekday() < 5 and now.hour == 23 and now.minute >= 25):
            toast('5 minutes until forced shutdown', 
                'Close your apps and save your work.')
            time.sleep(300)
            close_apps()
            shutdown()

def test_closure():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] in terminate_apps:
            print(proc.info['name'])
            proc.terminate()    
        # toast('5 minutes until forced shutdown', 
        # 'Close your apps and save your work. ')


def main():
    week_day_shutoff()

if __name__ == "__main__":
    main()