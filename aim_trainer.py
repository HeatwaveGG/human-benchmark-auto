import pyautogui
import keyboard

keyboard.wait("F8")
pyautogui.click(950, 400)

"""
area corners

449 190
1471 190
1471 673
449 673
"""

left = 449
right = 1471
top = 190
bottom = 673
step = 39
circle_colour = (149, 195, 232)
white = (255, 255, 255)

for i in range(30):
    found = False
    screenshot = pyautogui.screenshot()
    for row in range((bottom - top) // step + 1):
        if found:
            break  
        for col in range((right - left) // step + 1):

            current_x = left + col * step + step//2
            current_y = top + row * step + step//2

            color = screenshot.getpixel((current_x, current_y))

            if color == circle_colour or color == white:
                pyautogui.click(current_x, current_y)
                found = True
                break
                