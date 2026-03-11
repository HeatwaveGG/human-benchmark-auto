import pyautogui
import keyboard

count = 1

keyboard.wait("F8")

pyautogui.click(1790, 578)

starting_colour = pyautogui.pixel(1790, 578) # Red

while count <= 5:
    if pyautogui.pixel(1790, 578) != starting_colour:
        pyautogui.click()
        pyautogui.click()
        count += 1
