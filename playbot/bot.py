#========================Code by FRNINEZY====================================
#========================For more cheak out my github========================
import os 
import time 
import subprocess
import pyautogui
from selenium import webdriver
from colorama import Fore
from colorama import init


#colors 
g = Fore.GREEN
w = Fore.WHITE
c = Fore.LIGHTCYAN_EX
r = Fore.RED
m = Fore.LIGHTMAGENTA_EX

#init Foncion for colorama
init()

#cleaning cmd
os.system("cls")

print(m)
print(""" 
  _____  _                 _           _   
 |  __ \| |               | |         | |  
 | |__) | | __ _ _   _ ___| |__   ___ | |_ 
 |  ___/| |/ _` | | | / __| '_ \ / _ \| __|
 | |    | | (_| | |_| \__ \ |_) | (_) | |_ 
 |_|    |_|\__,_|\__, |___/_.__/ \___/ \__|
                  __/ |                    
                 |___/      """)








#input
print(w + "[" + g + "#" + w +"]" + c + "Enter link ")
print(w)
link = input("> ")
print(w + "<======================================"+ g + "Starting bot" + w +"======================================>")
time.sleep(3)
print(c + "Url => " + w + link)

#start bot 
d = webdriver.Chrome()
while True:
    print(w)
    d.get(link)
    pyautogui.press("space")
    time.sleep(30)
    d.refresh()