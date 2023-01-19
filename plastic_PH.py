import pyautogui
import time
from def_for_PH_batch_T1_second_PC import delay_standart, delay_standart_medium,\
    check_button_on_screen, click_on_center_button, check_button_on_screen_on_for_short

eyes_size_l_point = 1238, 289
eyes_size_r_point = 1423, 289

eyes_height_l_point =1238, 324
eyes_height_r_point =1423, 324
def open_plastic():
    pyautogui.press('f2')
    delay_standart()
    pyautogui.hotkey('shift', 'ctrl', 'x')
    check_button_on_screen('buttons2pc\\check_plastic.png')
    delay_standart()
    pyautogui.press('a')

def plastic_face(wight_face = '0', jaw_line = '0', chin_height = '0', eyes_size_l = '0',
                 eyes_size_r = '0', eyes_height_l = '0', eyes_height_r = '0'):

    bt0 = check_button_on_screen_on_for_short('buttons2pc\\no_face.png')
    if bt0 is not None:
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        pyautogui.press('esc')
        delay_standart()
    else:
        pyautogui.moveTo(100, 100)  # убрираем курсор мыши, что бы случайно не загородил интерфейс
        bt1 = check_button_on_screen('buttons2pc\\width_face.png', for_confidence=.9)
        click_on_center_button(bt1)
        delay_standart()
        pyautogui.write(wight_face)
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        bt2 = check_button_on_screen('buttons2pc\\jaw_line.png', for_confidence=.9)
        click_on_center_button(bt2)
        delay_standart()
        pyautogui.write(jaw_line)
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        bt3 = check_button_on_screen('buttons2pc\\chin_height.png', for_confidence=.9)
        click_on_center_button(bt3)
        delay_standart()
        pyautogui.write(chin_height)
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        pyautogui.moveTo(eyes_size_l_point)
        delay_standart()
        pyautogui.click()
        pyautogui.write(eyes_size_l)
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        pyautogui.moveTo(eyes_size_r_point)
        delay_standart()
        pyautogui.click()
        pyautogui.write(eyes_size_r)
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        pyautogui.moveTo(eyes_height_l_point)
        delay_standart()
        pyautogui.click()
        pyautogui.write(eyes_height_l)
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        pyautogui.moveTo(eyes_height_r_point)
        delay_standart()
        pyautogui.click()
        pyautogui.write(eyes_height_r)
        delay_standart()
        pyautogui.press('enter')
        delay_standart()
        delay_standart_medium()
        pyautogui.press('enter')





time.sleep(6)
open_plastic()
plastic_face(wight_face = '-10', jaw_line = '-20', eyes_size_l = '5',eyes_size_r = '3', eyes_height_l = '3',
             eyes_height_r = '3' )










