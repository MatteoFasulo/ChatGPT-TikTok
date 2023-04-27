import pyautogui
from time import sleep



for _ in range(10):
    x, y = pyautogui.position()

    print(f" x={x}, y={y}")
    sleep(1)