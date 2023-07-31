import keyboard
import pyautogui

def onpress(event):
    if event.name == "end":
        pyautogui.rightClick()

keyboard.on_press(callback=onpress)

keyboard.wait('esc')  # Wait for the "Escape" key to be pressed to exit the program
