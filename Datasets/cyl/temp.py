import pyautogui
import keyboard


def on_press(key):
    print(key.name)
    if key.name == "end":
        pyautogui.rightClick()


keyboard.on_press(on_press)
while True:
    pass