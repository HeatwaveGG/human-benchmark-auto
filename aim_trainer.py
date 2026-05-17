import pyautogui
import keyboard
import math

keyboard.wait("F8")
pyautogui.click(950, 400)

"""
area corners

449 190
1471 190
1471 673
449 673
"""

def colour_distance(c1, c2):
    return math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)

# Target circle diameter is 100

left = 517
right = 1471
top = 229
bottom = 673
step = 50
circle_colour = (149, 195, 232)
background = (43, 135, 209)

for i in range(30):
    found = False
    screenshot = pyautogui.screenshot()
    for row in range((bottom - top) // step + 1):
        if found:
            break  
        for col in range((right - left) // step + 1):
            current_x = left + col * step + step // 2
            current_y = top + row * step + step // 2
            color = screenshot.getpixel((current_x, current_y))
            if colour_distance(color, background) > 30:
                pyautogui.click(current_x, current_y)
                found = True
                break
                