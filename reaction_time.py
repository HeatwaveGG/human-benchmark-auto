import pyautogui
import keyboard

count = 1

keyboard.wait("F8")

pyautogui.click()

x, y = pyautogui.position()
starting_colour = pyautogui.pixel(x, y) # Red

while count <= 5:
    if pyautogui.pixel(x, y) != starting_colour:
        pyautogui.click()
        pyautogui.click()
        count += 1

print ("End")