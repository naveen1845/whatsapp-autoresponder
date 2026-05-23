import pyautogui
import time

try:
    while True:
        # Get coordinates
        x, y = pyautogui.position()
        
        # Format string to overwrite the current line
        position_str = f"X: {x:4} Y: {y:4}"
        print(position_str, end="\r", flush=True)
        
        time.sleep(0.05)  # Small delay to reduce CPU usage
except KeyboardInterrupt:
    print("\nDone.")

'''
Run this file to get the cordinates of the mouse so as to perform operations to select, copy/paste stuff from the screen and send the messages

my observations
DRAG
from 409 129
to 409 853

TO PASTE -> 743 876
to SEND -> 1443 875 or hit enter on keyboard
'''