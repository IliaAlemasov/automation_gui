import time
import keyboard
import pyautogui

def check_button_on_screen(button_path: str, for_grayscale=True, for_confidence=.7 ):
    while True:
        button = pyautogui.locateOnScreen(button_path, grayscale=for_grayscale, confidence=for_confidence)
        if button is not None:
            return (button)
        else:
            pass
        time.sleep(.7) #пауза для оптимизации While


def click_on_center_button(button_x_y):
    center_button = pyautogui.center(button_x_y)
    pyautogui.leftClick(center_button)


def apply_nik():
    button = check_button_on_screen('buttons\\apply.png',for_confidence=.9)
    print(button)
    click_on_center_button(button)

time.sleep(10)

apply_nik()






