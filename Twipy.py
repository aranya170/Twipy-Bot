from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(3)

while True:
    keyboard.press('j')
    keyboard.release('j')

    time.sleep(0.1)
    keyboard.press('l')
    keyboard.release('l')
    time.sleep(1)
