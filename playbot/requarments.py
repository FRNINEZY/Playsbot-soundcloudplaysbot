import os 
import subprocess
import time
from datetime import date


t = date.today()
d = t.strftime("%B %d, %Y")

#cleaning terminal
os.system("clear")

#Starting 
print("Hello installing requarments for bot")
time.sleep(4)
print("")
print("Startign Date is ==> " + d)

#Installing 
print("Installing Colorama")
print("")
subprocess.run(["pip", "install", "colorama"])
print("")
print("[2] Colorama => Done")
print("")
time.sleep(3)

print("Installing Selenium")
print("")
subprocess.run(["pip", "install", "selenium"])
print("")
print("[3] Selenium => Done")
print("")
time.sleep(3)

print("Installing pyautogui")
print("")
subprocess.run(["pip", "install", "PyAutoGUI"])
print("")
print("[4] pyautogui => Done")

os.system("cls")

print("Done now you can run bot.py")