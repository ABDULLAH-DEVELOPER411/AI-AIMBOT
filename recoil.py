import pyautogui
import time
import win32api
import random
import keyboard
import os

print("[RECOIL REDUCER] This cheat was made by bl5ze")
print("")

print("[RECOIL REDUCER] Enter desired vertical strength (recommended 1-10)")
def prompt(str):
        valid_input = False
        while not valid_input:
            try:
                number = float(input(str))
                valid_input = True
            except ValueError:
                print("[!] Invalid Input. Make sure to enter only the number (e.g. 3.5)")
        return number

verticalstrength = prompt("[RECOIL REDUCER] Vertical Strength: ")

print("")

print("[RECOIL REDUCER] Enter desired horizontal strength (recommended 1-10)")
horizontalstrength = prompt("[RECOIL REDUCER] Horizontal Strength: ")

print("")

print("[RECOIL REDUCER] Settings configuration completed successfully..")

print("")

time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

recoilcontrolenabled = True
minverticalstrength = verticalstrength / 2

clicked = False

def is_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

while True:   
    if is_mouse_down() and recoilcontrolenabled:

        
        offsetconst = 1000

        minverticalstrength = verticalstrength / 2
        horizontaloffset = random.randrange(-horizontalstrength * offsetconst, horizontalstrength * offsetconst, 1) / offsetconst
        verticaloffset = random.randrange(minverticalstrength * offsetconst, verticalstrength * offsetconst, 1) / offsetconst
        
        win32api.mouse_event(0x0001, int(horizontaloffset), int(verticaloffset))

        time_offset = random.randrange(0.02 * offsetconst, 0.05 * offsetconst, 1) / offsetconst
        time.sleep(time_offset)

        if clicked == False:
            os.system('cls' if os.name == 'nt' else 'clear')
            clicked = True


    time.sleep(0.001)