import time
import keyboard
import pyautogui


def apply_nik():
    while True:
        r = pyautogui.locateOnScreen('apply.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
        time.sleep(0.7)

def open_partiture(): # запуск партируры
    pyautogui.moveTo(871, 24)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.51)
    pyautogui.moveTo(1147, 870)
    time.sleep(0.51)
    pyautogui.moveTo(1533, 878)
    time.sleep(0.51)
    pyautogui.leftClick()

def open_nik(): #запуск плагинов никон
    pyautogui.moveTo(871, 24)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.51)
    pyautogui.moveTo(927, 918)
    time.sleep(0.51)
    pyautogui.moveTo(1591, 916)
    time.sleep(0.51)
    pyautogui.moveTo(1587, 948)
    time.sleep(0.51)
    pyautogui.leftClick()
    time.sleep(3) #пауза для загрузки окна плагинов
    while True: # проверка на окно обновлений и его закрытие
        r = pyautogui.locateOnScreen('update.png', grayscale=True, confidence=.7)
        if r is not None:
            pyautogui.press('Esc')
            break
        else:
            r = None
        time.sleep(0.7)


keyboard.add_hotkey('ctrl+v', apply_nik)

keyboard.add_hotkey('ctrl+h', open_partiture)

keyboard.add_hotkey('pause', open_nik)

keyboard.wait()
