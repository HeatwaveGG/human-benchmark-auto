import pyautogui
import keyboard

keyboard.wait("F8")

pyautogui.click()

level = 1

"""
Logic:

make a list to simulate the squares
associate 1 pair of coords to 1 square
have the starting colour of the squares

loop:
check the colour of each square (each coord associated with the square)
when a colour changes from its original colour in a pair of coords, convert the coords into a square and add it to a list 
stop checking the colour after a set amount of time has passed
go over the list and click the corresponding coordinates
clear the list

"""