import ctypes
import cv2
import json
import math
import mss
import numpy as np
import os
import sys
import time
import torch
import uuid
import win32api

import pathlib
from pathlib import Path
pathlib.PosixPath = pathlib.WindowsPath

from termcolor import colored

class config:
        with open("lib/config/configuration.json") as f:
         config = json.load(f)

if config.config["aimkey"] == "leftShift":
    def is_targeted():
        return True if win32api.GetKeyState(0xA0) in (-127, -128) else False
elif config.config["aimkey"] == "leftAlt":
     def is_targeted():
        return True if win32api.GetKeyState(0x12) in (-127, -128) else False
elif config.config["aimkey"] == "rightMouse":
    def is_targeted():
        return True if win32api.GetKeyState(0x02) in (-127, -128) else False
elif config.config["aimkey"] == "middleMouse":
    def is_targeted():
        return True if win32api.GetKeyState(0x04) in (-127, -128) else False
elif config.config["aimkey"] == "mouse5":
     def is_targeted():
        return True if win32api.GetKeyState(0x06) in (-127, -128) else False
elif config.config["aimkey"] == "leftMouse":
     def is_targeted():
        return True if win32api.GetKeyState(0x01) in (-127, -128) else False
elif config.config["aimkey"] == "ctrl":
     def is_targeted():
        return True if win32api.GetKeyState(0x11) in (-127, -128) else False
elif config.config["aimkey"] == "mouse4":
     def is_targeted():
        return True if win32api.GetKeyState(0x5) in (-127, -128) else False
elif config.config["aimkey"] == "`":
     def is_targeted():
        return True if win32api.GetKeyState(0xC0) in (-127, -128) else False
elif config.config["aimkey"] == "1":
     def is_targeted():
        return True if win32api.GetKeyState(0x31) in (-127, -128) else False
elif config.config["aimkey"] == "2":
     def is_targeted():
        return True if win32api.GetKeyState(0x32) in (-127, -128) else False
elif config.config["aimkey"] == "3":
     def is_targeted():
        return True if win32api.GetKeyState(0x33) in (-127, -128) else False
elif config.config["aimkey"] == "4":
     def is_targeted():
        return True if win32api.GetKeyState(0x34) in (-127, -128) else False
elif config.config["aimkey"] == "5":
     def is_targeted():
        return True if win32api.GetKeyState(0x35) in (-127, -128) else False
elif config.config["aimkey"] == "6":
     def is_targeted():
        return True if win32api.GetKeyState(0x36) in (-127, -128) else False
elif config.config["aimkey"] == "7":
     def is_targeted():
        return True if win32api.GetKeyState(0x37) in (-127, -128) else False
elif config.config["aimkey"] == "8":
     def is_targeted():
        return True if win32api.GetKeyState(0x38) in (-127, -128) else False
elif config.config["aimkey"] == "9":
     def is_targeted():
        return True if win32api.GetKeyState(0x39) in (-127, -128) else False
elif config.config["aimkey"] == "0":
     def is_targeted():
        return True if win32api.GetKeyState(0x30) in (-127, -128) else False
elif config.config["aimkey"] == "-":
     def is_targeted():
        return True if win32api.GetKeyState(0xBD) in (-127, -128) else False
elif config.config["aimkey"] == "Q":
     def is_targeted():
        return True if win32api.GetKeyState(0x51) in (-127, -128) else False
elif config.config["aimkey"] == "capsLock":
     def is_targeted():
        return True if win32api.GetKeyState(0x14) in (-127, -128) else False
elif config.config["aimkey"] == "W":
     def is_targeted():
        return True if win32api.GetKeyState(0x57) in (-127, -128) else False
elif config.config["aimkey"] == "E":
     def is_targeted():
        return True if win32api.GetKeyState(0x45) in (-127, -128) else False
elif config.config["aimkey"] == "R":
     def is_targeted():
        return True if win32api.GetKeyState(0x52) in (-127, -128) else False
elif config.config["aimkey"] == "T":
     def is_targeted():
        return True if win32api.GetKeyState(0x54) in (-127, -128) else False
elif config.config["aimkey"] == "Y":
     def is_targeted():
        return True if win32api.GetKeyState(0x59) in (-127, -128) else False
elif config.config["aimkey"] == "U":
     def is_targeted():
        return True if win32api.GetKeyState(0x55) in (-127, -128) else False
elif config.config["aimkey"] == "I":
     def is_targeted():
        return True if win32api.GetKeyState(0x49) in (-127, -128) else False
elif config.config["aimkey"] == "O":
     def is_targeted():
        return True if win32api.GetKeyState(0x59) in (-127, -128) else False
elif config.config["aimkey"] == "P":
     def is_targeted():
        return True if win32api.GetKeyState(0x50) in (-127, -128) else False
elif config.config["aimkey"] == "[":
     def is_targeted():
        return True if win32api.GetKeyState(0xDB) in (-127, -128) else False
elif config.config["aimkey"] == "]":
     def is_targeted():
        return True if win32api.GetKeyState(0xDD) in (-127, -128) else False
elif config.config["aimkey"] == "A":
     def is_targeted():
        return True if win32api.GetKeyState(0x41) in (-127, -128) else False
elif config.config["aimkey"] == "S":
     def is_targeted():
        return True if win32api.GetKeyState(0x53) in (-127, -128) else False
elif config.config["aimkey"] == "D":
     def is_targeted():
        return True if win32api.GetKeyState(0x44) in (-127, -128) else False
elif config.config["aimkey"] == "F":
     def is_targeted():
        return True if win32api.GetKeyState(0x46) in (-127, -128) else False
elif config.config["aimkey"] == "G":
     def is_targeted():
        return True if win32api.GetKeyState(0x47) in (-127, -128) else False
elif config.config["aimkey"] == "H":
     def is_targeted():
        return True if win32api.GetKeyState(0x48) in (-127, -128) else False
elif config.config["aimkey"] == "J":
     def is_targeted():
        return True if win32api.GetKeyState(0x4A) in (-127, -128) else False
elif config.config["aimkey"] == "K":
     def is_targeted():
        return True if win32api.GetKeyState(0x4B) in (-127, -128) else False
elif config.config["aimkey"] == "L":
     def is_targeted():
        return True if win32api.GetKeyState(0x4C) in (-127, -128) else False
elif config.config["aimkey"] == ";":
     def is_targeted():
        return True if win32api.GetKeyState(0xBA) in (-127, -128) else False
elif config.config["aimkey"] == "'":
     def is_targeted():
        return True if win32api.GetKeyState(0xDE) in (-127, -128) else False
elif config.config["aimkey"] == "\ ":
     def is_targeted():
        return True if win32api.GetKeyState(0xDC) in (-127, -128) else False
elif config.config["aimkey"] == "Z":
     def is_targeted():
        return True if win32api.GetKeyState(0x5A) in (-127, -128) else False
elif config.config["aimkey"] == "X":
     def is_targeted():
        return True if win32api.GetKeyState(0x58) in (-127, -128) else False
elif config.config["aimkey"] == "C":
     def is_targeted():
        return True if win32api.GetKeyState(0x43) in (-127, -128) else False
elif config.config["aimkey"] == "V":
     def is_targeted():
        return True if win32api.GetKeyState(0x56) in (-127, -128) else False
elif config.config["aimkey"] == "B":
     def is_targeted():
        return True if win32api.GetKeyState(0x42) in (-127, -128) else False
elif config.config["aimkey"] == "N":
     def is_targeted():
        return True if win32api.GetKeyState(0x4E) in (-127, -128) else False
elif config.config["aimkey"] == "M":
     def is_targeted():
        return True if win32api.GetKeyState(0x4D) in (-127, -128) else False
elif config.config["aimkey"] == ",":
     def is_targeted():
        return True if win32api.GetKeyState(0xBC) in (-127, -128) else False
elif config.config["aimkey"] == ".":
     def is_targeted():
        return True if win32api.GetKeyState(0xBE) in (-127, -128) else False
elif config.config["aimkey"] == "/ ":
     def is_targeted():
        return True if win32api.GetKeyState(0xBF) in (-127, -128) else False

model_path = config.config["model_path"]
confidence = config.config["confidence"]
fovsize = config.config["fovsize"]
mousedelay = config.config["mouse_delay"]
pixelincrement = config.config["pixel_increment"]
smoothing_enabled = config.config["smoothing_enabled"]
smoothness = config.config["smoothness"]
triggerbot = config.config["triggerbot"]
triggerbot_threshold = config.config["triggerbot_threshold"]
aimheight = config.config["aimheight"]
ai_vision = config.config["ai_vision"]

smoothing = smoothness / 10

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

class Aimbot:
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    screen = mss.mss()
    pixel_increment = pixelincrement #controls how many pixels the mouse moves for each relative movement
    with open("lib/config/sensitivity.json") as f:
        sens_config = json.load(f)
    aimbot_status = colored("ENABLED", 'blue')

    def __init__(self, box_constant = fovsize, collect_data = True, mouse_delay = mousedelay, debug = False):
        #controls the initial centered box width and height of the "Vision" window
        self.box_constant = box_constant #controls the size of the detection box (equaling the width and height)

        print("[INTERSTELLAR] Loading the cheat and implementing the AI..")
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload = True)
        if torch.cuda.is_available():
            print(colored("CUDA ACCELERATION [ENABLED]", "green"))
        else:
            print(colored("[!] CUDA ACCELERATION IS UNAVAILABLE", "red"))
            print(colored("[!] Check your PyTorch installation, or else performance will be poor", "red"))

        self.max_det = 1
        self.model.conf = confidence # base confidence threshold (or base detection (0-1)
        self.model.iou = 0.01 # NMS IoU (0-1)
        self.collect_data = collect_data
        self.debug = debug
        self.mouse_delay = mouse_delay

        print(colored("\n[INTERSTELLAR] Keybinds:\n[ F1 ] - TOGGLE AIMBOT\n[ F2 ] - QUIT/PANIC", "white"))
        print("[",config.config["aimkey"],"] - YOUR AIMKEY")
        print(" ")
    
    def update_status_aimbot():
        if Aimbot.aimbot_status == colored("ENABLED", 'blue'):
            Aimbot.aimbot_status = colored("DISABLED", 'red')
        else:
            Aimbot.aimbot_status = colored("ENABLED", 'blue')
        sys.stdout.write("\033[K")
        print(f"[INTERSTELLAR] AIMBOT IS [{Aimbot.aimbot_status}]", end = "\r")

    def left_click():
        ctypes.windll.user32.mouse_event(0x0002) # left mouse down
        Aimbot.sleep(0.0001)
        ctypes.windll.user32.mouse_event(0x0004) # left mouse up
    

    def sleep(duration, get_now = time.perf_counter):
        if duration == 0: return
        now = get_now()
        end = now + duration
        while now < end:
            now = get_now()

    def is_aimbot_enabled():
        return True if Aimbot.aimbot_status == colored("ENABLED", 'blue') else False


    def is_target_locked(x, y):
        #plus/minus 5 pixel threshold
        threshold = triggerbot_threshold
        return True if 960 - threshold <= x <= 960 + threshold and 540 - threshold <= y <= 540 + threshold else False   

    def move_crosshair(self, x, y):
        if is_targeted():
            scale = Aimbot.sens_config["targeting_scale"]
        else:
            return #TODO

        if self.debug: start_time = time.perf_counter()
        for rel_x, rel_y in Aimbot.interpolate_coordinates_from_center((x, y), scale):
            Aimbot.ii_.mi = MouseInput(rel_x, rel_y, 0, 0x0001, 0, ctypes.pointer(Aimbot.extra))
            input_obj = Input(ctypes.c_ulong(0), Aimbot.ii_)
            ctypes.windll.user32.SendInput(1, ctypes.byref(input_obj), ctypes.sizeof(input_obj))
            if self.mouse_delay > 0:
                if not self.debug: Aimbot.sleep(self.mouse_delay) #time.sleep is not accurate enough
        if self.debug: #remove this later
            print(f"TIME: {time.perf_counter() - start_time}")
            print("DEBUG: SLEEPING FOR 1 SECOND")
            time.sleep(1)

    #generator yields pixel tuples for relative movement
    def interpolate_coordinates_from_center(absolute_coordinates, scale):
        diff_x = (absolute_coordinates[0] - 960) * scale/Aimbot.pixel_increment
        diff_y = (absolute_coordinates[1] - 540) * scale/Aimbot.pixel_increment
        if smoothing_enabled == 1:
            length = int(math.dist((0,0), (diff_x * smoothing, diff_y * smoothing)))
        else:
            length = int(math.dist((0,0), (diff_x, diff_y)))
        if length == 0: return
        unit_x = (diff_x/length) * Aimbot.pixel_increment
        unit_y = (diff_y/length) * Aimbot.pixel_increment
        x = y = sum_x = sum_y = 0
        for k in range(0, length):
            sum_x += x
            sum_y += y
            x, y = round(unit_x * k - sum_x), round(unit_y * k - sum_y)
            yield x, y
            

    def start(self):
        Aimbot.update_status_aimbot()
        half_screen_width = ctypes.windll.user32.GetSystemMetrics(0)/2 # this should always be 960
        half_screen_height = ctypes.windll.user32.GetSystemMetrics(1)/2 #this should always be 540
        detection_box = {'left': int(half_screen_width - self.box_constant//2), #x1 coord (for top-left corner of the box)
                          'top': int(half_screen_height - self.box_constant//2), #y1 coord (for top-left corner of the box)
                          'width': int(self.box_constant),  #width of the box
                          'height': int(self.box_constant)} #height of the box
        if self.collect_data:
            collect_pause = 0

        while True:
            start_time = time.perf_counter()
            frame = np.array(Aimbot.screen.grab(detection_box))
            if self.collect_data: orig_frame = np.copy((frame))
            results = self.model(frame)

            if len(results.xyxy[0]) != 0: #player detected
                least_crosshair_dist = closest_detection = player_in_frame = False
                for *box, conf, cls in results.xyxy[0]: #iterate over each player detected
                    x1y1 = [int(x.item()) for x in box[:2]]
                    x2y2 = [int(x.item()) for x in box[2:]]
                    x1, y1, x2, y2, conf = *x1y1, *x2y2, conf.item()
                    height = y2 - y1
                    relative_position_X, relative_position_Y = int((x1 + x2)/2), int((y1 + y2)/2 - height/aimheight) #offset to roughly approximate the position using a ratio of the height
                    
                    if fovsize > 250:
                        own_player = x1 < 15 or (x1 < self.box_constant/5 and y2 > self.box_constant/1.2) #helps ensure that your own player is not regarded as a valid detection

                    #calculate the distance between each detection and the crosshair at (self.box_constant/2, self.box_constant/2)
                    crosshair_dist = math.dist((relative_position_X, relative_position_Y), (self.box_constant/2, self.box_constant/2))

                    if not least_crosshair_dist: least_crosshair_dist = crosshair_dist #initalize least crosshair distance variable first iteration

                    if crosshair_dist <= least_crosshair_dist:
                        least_crosshair_dist = crosshair_dist
                        closest_detection = {"x1y1": x1y1, "x2y2": x2y2, "relative_position_X": relative_position_X, "relative_position_Y": relative_position_Y, "conf": conf}
                    
                    if not own_player:
                        cv2.rectangle(frame, x1y1, x2y2, (255, 255, 255), 2) #draw the bounding boxes for all of the player detections (except own)
                        cv2.putText(frame, f"{int(conf * 100)}%", x1y1, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255)) #draw the confidence labels on the bounding boxes
                    else:
                        own_player = False
                        if not player_in_frame:
                            player_in_frame = True

                if closest_detection: #if valid detection exists

                    if fovsize > 250:
                        own_player = x1 < 15 or (x1 < self.box_constant/5 and y2 > self.box_constant/1.2) #helps ensure that your own player is not regarded as a valid detection
                    
                    #draw line from the crosshair to the position
                    if not own_player:
                        cv2.line(frame, (closest_detection["relative_position_X"], closest_detection["relative_position_Y"]), (self.box_constant//2, self.box_constant//2), (255, 255, 255), 2)

                    if not own_player:
                        absolute_position_X, absolute_position_Y = closest_detection["relative_position_X"] + detection_box['left'], closest_detection["relative_position_Y"] + detection_box['top']

                    if not own_player:
                        x1, y1 = closest_detection["x1y1"]
                        if Aimbot.is_target_locked(absolute_position_X, absolute_position_Y):
                            if triggerbot == 1  and Aimbot.is_aimbot_enabled():
                                Aimbot.left_click()
                            cv2.putText(frame, "", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255), 2) #draw the confidence labels on the bounding boxes
                        else:
                            cv2.putText(frame, "", (x1 + 40, y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255,255,255), 2) #draw the confidence labels on the bounding boxes

                    if not own_player:
                        if Aimbot.is_aimbot_enabled():
                            Aimbot.move_crosshair(self, absolute_position_X, absolute_position_Y)

            if self.collect_data and time.perf_counter() - collect_pause > 1 and Aimbot.is_targeted() and Aimbot.is_aimbot_enabled() and not player_in_frame: #screenshots can only be taken every 1 second
                cv2.imwrite(f"lib/data/{str(uuid.uuid4())}.jpg", orig_frame)
                collect_pause = time.perf_counter()
            cv2.putText(frame, f"{int(1/(time.perf_counter() - start_time)) * 4.5 }", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
            if ai_vision == 1:
                cv2.imshow("AI Vision", frame)
                
            if cv2.waitKey(1) & 0xFF == ord('0'):
                break

    def clean_up():
        print(colored("\n[INTERSTELLAR] Aimbot is CLOSING...", "red"))
        Aimbot.screen.close()
        os._exit(0)

if __name__ == "__main__": print("Error")