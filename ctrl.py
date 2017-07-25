"""
text-based UI for a rasberry pi robot
"""

import curses
import time
from RPi import GPIO

FWD = 1
BCK = 2
STOP = 3

LEFT = (23, 24, 25)
RIGHT = (16, 20, 21)

def set_pin(pin, value):
    print("set_pin", pin, value)
    if value:
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)

def go_wheel(wheel, d):
    if d == FWD:
        set_pin(wheel[1], 1)
        set_pin(wheel[2], 0)
    elif d == BCK:
        set_pin(wheel[1], 0)
        set_pin(wheel[2], 1)
        
    if d == STOP:
        set_pin(wheel[0], 0)
    else:
        set_pin(wheel[0], 1)
        
def go(ldir, rdir):
    go_wheel(LEFT, ldir)
    go_wheel(RIGHT, rdir)
    time.sleep(.1)
    go_wheel(LEFT, STOP)
    go_wheel(RIGHT, STOP)

def main(win):
    curses.noecho()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEFT, GPIO.OUT)
    GPIO.setup(RIGHT, GPIO.OUT)    
    while True:
        ch = win.getch()
        if ch == curses.KEY_RIGHT:
            go(FWD, BCK)
        elif ch == curses.KEY_LEFT:
            go(BCK, FWD)
        elif ch == curses.KEY_UP:
            go(FWD, FWD)
        elif ch == curses.KEY_DOWN:
            go(BCK, BCK)
        else:
            pass

try:
    curses.wrapper(main)
finally:
    GPIO.cleanup()
    


