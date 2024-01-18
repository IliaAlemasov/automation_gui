import time
import keyboard
import pyautogui
from def_for_PH_batch_T2 import *

def del_and_shift():
    button = check_button_on_screen ('buttons\\del_and_shift.png',for_confidence=.7)
    delay_before_click()
    click_on_center_button(button)
    #delay_before_click()
    #pyautogui.press('v')
    #delay_before_click()
    pyautogui.moveTo(1953,1735)

keyboard.add_hotkey('tab ', del_and_shift)

keyboard.wait()