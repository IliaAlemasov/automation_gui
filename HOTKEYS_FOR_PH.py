import time
import keyboard
import pyautogui

'''Script for create custom hot keys. Up speed and comfort your work
 in typical action. Save your cognitive resource and work with pleasure.
 For example building my hot keys for Photoshop'''

#-----base def & value XY for constration-----#

def delay_before_click(): #пауза перед кликом
    time.sleep(0.1)

def delay_drop_dawn_list():#пауза для раскрытия выпадающих списков
    time.sleep(.51)

def check_button_on_screen(button_path: str, for_grayscale=True, for_confidence=.9 ):
    while True:
        button = pyautogui.locateOnScreen(button_path, grayscale=for_grayscale, confidence=for_confidence)
        if button is not None:
            return (button)
        else:
            pass
        time.sleep(.7) #пауза для оптимизации While

def check_button_on_screen_on_for(button_path: str, for_grayscale=True, for_confidence=.9 ):
    for i in range(40):
        button = pyautogui.locateOnScreen(button_path, grayscale=for_grayscale, confidence=for_confidence)
        if button is not None:
            return (button)
        else:
            pass
        time.sleep(.7) #пауза для оптимизации for

def click_on_center_button(button_box):
    center_button = pyautogui.center(button_box)
    pyautogui.leftClick(center_button)


xy_open_partiture1 = (871, 24) # координаты кнопок для открытия partiture
xy_open_partiture2 = (1147, 870)
xy_open_partiture3 = (1533, 878)

xy_open_nik1 = (871, 24) # координаты кнопок для открытия nik
xy_open_nik2 = (927, 918)
xy_open_nik3 = (1591, 916)
xy_open_nik4 = (1587, 948)

#-----functional def for hotkeys binds-----#

def apply_nik():
    button = check_button_on_screen('buttons\\apply.png',for_confidence=.9)
    click_on_center_button(button)
def open_partiture(): # запуск партируры
    pyautogui.moveTo(xy_open_partiture1)
    delay_before_click()
    pyautogui.leftClick()
    delay_drop_dawn_list()
    pyautogui.moveTo(xy_open_partiture2)
    delay_drop_dawn_list()
    pyautogui.moveTo(xy_open_partiture3)
    delay_drop_dawn_list()
    pyautogui.leftClick()

def open_nik(): #запуск плагинов никон
    pyautogui.moveTo(xy_open_nik1)
    delay_before_click()
    pyautogui.leftClick()
    delay_drop_dawn_list()
    pyautogui.moveTo(xy_open_nik2)
    delay_drop_dawn_list()
    pyautogui.moveTo(xy_open_nik3)
    delay_drop_dawn_list()
    pyautogui.moveTo(xy_open_nik4)
    delay_drop_dawn_list()
    pyautogui.leftClick()
    time.sleep(3) #пауза для загрузки окна плагинов
    check_button_on_screen_on_for('buttons\\update.png')
    if check_button_on_screen_on_for is not None:
        pyautogui.press('Esc')
    else:
        check_button_on_screen_on_for is None
        pass

#-----Binds def on hotkey-----#
if __name__ == '__main__':

    keyboard.add_hotkey('ctrl+v', apply_nik)

    keyboard.add_hotkey('ctrl+h', open_partiture)

    keyboard.add_hotkey('pause', open_nik)

    keyboard.wait()
