import pyautogui
import keyboard
import time

# squares in grid
square1 = (818, 307)
square2 = (951, 297)
square3 = (1074, 319)
square4 = (832, 441)
square5 = (951, 435)
square6 = (1092, 432)
square7 = (816, 551)
square8 = (945, 587)
square9 = (1071, 573)
squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9]
level = 1

keyboard.wait("F8")
pyautogui.click(957, 550) # clicks the start

while True:
    sequence = []
    squareNumber = 1
    prev_frames = ["not white"] * 9

    while len(sequence) < level:  # Keeps tracking until the length of the sequence is the same as the level number
        for square in squares:
            if pyautogui.pixel(*square) == (255, 255, 255) and prev_frames[squareNumber - 1] == "not white":
                sequence.append("square" + str(squareNumber))
                prev_frames[squareNumber - 1] = "white"
            elif pyautogui.pixel(*square) != (255, 255, 255):
                prev_frames[squareNumber - 1] = "not white"

            squareNumber += 1

            if squareNumber > 9:
                squareNumber = 1
                
    time.sleep(0.5)
    for click in sequence:
        match click:
            case "square1":
                pyautogui.click(*square1)
            case "square2":
                pyautogui.click(*square2)
            case "square3":
                pyautogui.click(*square3)
            case "square4":
                pyautogui.click(*square4)
            case "square5":
                pyautogui.click(*square5)
            case "square6":
                pyautogui.click(*square6)
            case "square7":
                pyautogui.click(*square7)
            case "square8":
                pyautogui.click(*square8)
            case "square9":
                pyautogui.click(*square9)
        time.sleep(0.2)
    level += 1