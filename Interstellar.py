import json
import os
import sys
import threading

from pynput import keyboard
from termcolor import colored

from urllib.request import urlopen

def on_release(key):
    try:
        if key == keyboard.Key.f1:
            Aimbot.update_status_aimbot()
        if key == keyboard.Key.f2:
            Aimbot.clean_up()
    except NameError:
        pass

def main():
    global Interstellar
    Interstellar = Aimbot(collect_data = "collect_data" in sys.argv)
    Interstellar.start()

def setup():
    path = "lib/sensitivity"
    if not os.path.exists(path):
        os.makedirs(path)

    def prompt(str):
        valid_input = False
        while not valid_input:
            try:
                number = float(input(str))
                valid_input = True
            except ValueError:
                print("[!] Invalid Input. Make sure to enter only the number (e.g. 11.1)")
        return number

    xy_sens = prompt("XY Sensitivity: ")
    targeting_sens = prompt("ADS Sensitivity: ")
    sensitivity_settings = {"xy_sens": xy_sens, "targeting_sens": targeting_sens, "xy_scale": 10/xy_sens, "targeting_scale": 1000/(targeting_sens * xy_sens)}

    with open('lib/config/sensitivity.json', 'w') as outfile:
        json.dump(sensitivity_settings, outfile)
    print("[INTERSTELLAR] Sensitivity configuration complete")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

    print(colored('''
     ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███
    ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ █
    ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ 
    ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄ 
    ░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██ v1
    ░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓ 
     ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▓ 
     ▒ ░   ░   ░ ░   ░         ░     ░░   ░                                                                                                  
    - created by ABDULLAH
                  ''', "DEVELOPER"))

    path_exists = os.path.exists("lib/config/sensitivity.json")
    if not path_exists or ("setup" in sys.argv):
        if not path_exists:
            print("[!] Sensitivity configuration is not set")
        setup()
    path_exists = os.path.exists("lib/data")
    if "collect_data" in sys.argv and not path_exists:
        os.makedirs("lib/data")
    from lib.aimbot import Aimbot
    listener = keyboard.Listener(on_release=on_release)
    listener.start()
    main()