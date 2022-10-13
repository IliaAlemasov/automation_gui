import time
import pyautogui

def open_partiture(): # запуск партируры
    pyautogui.moveTo(871,24)
    time.sleep(0.1)
    pyautogui.leftClick()
    time.sleep(0.51)
    pyautogui.moveTo(1147, 870)
    time.sleep(0.51)
    pyautogui.moveTo(1533, 878)
    time.sleep(0.51)
    pyautogui.leftClick()

def load_partiture():# проверка на загрузку партритуры
    while True:
        r = pyautogui.locateOnScreen('por_icon.png', grayscale=True, confidence=.7)
        if r is not None:
            time.sleep(7)
            pyautogui.press('Enter')
            break
        else:
            r = None
        time.sleep(0.7)
    time.sleep(7)

def after_partiture25():# 25%
    pyautogui.hotkey('shift', 'ctrl', 'f12')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('f3')
    time.sleep(0.5)
    pyautogui.press('f2')
    time.sleep(0.5)

def after_partiture40():# 40%
    pyautogui.press('f11')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('f3')
    time.sleep(0.5)
    pyautogui.press('f2')
    time.sleep(0.5)


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
        r = pyautogui.locateOnScreen('update.png', grayscale=True, confidence=.9)
        if r is not None:
            pyautogui.press('Esc')
            break
        else:
            r = None
        time.sleep(0.7)

def custom_but_nik(): #кнопка custon nik
    while True:
        r = pyautogui.locateOnScreen('custom.png', grayscale=True)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
        time.sleep(0.7)
    time.sleep(0.5)

def target_filter1_nik(): #кнопка target filter1
    while True:
        r = pyautogui.locateOnScreen('custom1.png', grayscale=True, confidence=.8)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.moveTo(e)
            time.sleep(0.1)
            pyautogui.moveRel(0,-70)
            time.sleep(0.1)
            pyautogui.leftClick()
            break
        else:
            r = None
        time.sleep(0.7)
    time.sleep(8)#пауза для прогрузки предпросмотра фильтров

def target_filter2_nik(): #кнопка target filter2
    while True:
        r = pyautogui.locateOnScreen('custom2.png', grayscale=True, confidence=.8)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.moveTo(e)
            time.sleep(0.1)
            pyautogui.moveRel(0,-70)
            time.sleep(0.1)
            pyautogui.leftClick()
            break
        else:
            r = None
        time.sleep(0.7)
    time.sleep(8)#пауза для прогрузки предпросмотра фильтров

def target_filter3_nik(): #кнопка target filter3
    while True:
        r = pyautogui.locateOnScreen('custom3.png', grayscale=True, confidence=.8)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.moveTo(e)
            time.sleep(0.1)
            pyautogui.moveRel(0,-70)
            time.sleep(0.1)
            pyautogui.leftClick()
            break
        else:
            r = None
        time.sleep(0.7)
    time.sleep(8)#пауза для прогрузки предпросмотра фильтров

def target_filter4_nik(): #кнопка target filter4
    while True:
        r = pyautogui.locateOnScreen('custom4.png', grayscale=True, confidence=.8)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.moveTo(e)
            time.sleep(0.1)
            pyautogui.moveRel(0,-70)
            time.sleep(0.1)
            pyautogui.leftClick()
            break
        else:
            r = None
        time.sleep(0.7)
    time.sleep(8)#пауза для прогрузки предпросмотра фильтров

def target_filter5_nik(): #кнопка target filter5 + избраное
    for p in range(5):
        r = pyautogui.locateOnScreen('star.png', confidence=.95)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.moveTo(e)
            time.sleep(0.1)
            pyautogui.leftClick()
            break
        else:
            r = None
        time.sleep(0.7)
    while True:
        r = pyautogui.locateOnScreen('custom5.png', grayscale=True, confidence=.8)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.moveTo(e)
            time.sleep(0.1)
            pyautogui.moveRel(0,-70)
            time.sleep(0.1)
            pyautogui.leftClick()
            break
        else:
            r = None
        time.sleep(0.7)
    time.sleep(8)#пауза для прогрузки предпросмотра фильтров

def apply_nik():  #кнопка готово плагины никон
    while True:
        r = pyautogui.locateOnScreen('apply.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
        time.sleep(1)


def loading_pause():# пауза для прогрузки долгих операций
    time.sleep(28)

def loading_pause_short():# пауза для прогрузки долгих операций
    time.sleep(15)


def ph_levels1():# уровни стандарт 248,1.04,1
    pyautogui.press('f2')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'f12')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('f2')
    time.sleep(0.5)

def ph_levels2():# уровни + 245,1.06,1
    pyautogui.press('f2')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'f12')
    time.sleep(0.5)
    pyautogui.press('f2')
    time.sleep(0.5)

def ph_levels3():# уровни средние тона+ 1.1
    pyautogui.press('f2')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'f11')
    time.sleep(0.5)
    pyautogui.press('f2')
    time.sleep(0.5)

def copy_layer():
    pyautogui.press('f2')
    pyautogui.press('f2')

def color_correction1():
    pyautogui.press('f8')
    time.sleep(0.5)
    pyautogui.press('enter')

def color_correction2():
    pyautogui.hotkey('shift', 'f8')
    time.sleep(0.5)
    pyautogui.press('enter')




def open_foto(dir_name,file_nane): # y это путь к папке строкой, x - имя файла
    while True:#кнопка файл
        r = pyautogui.locateOnScreen('file.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
    time.sleep(0.6)
    while True:#кнопка open
        r = pyautogui.locateOnScreen('open.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
    time.sleep(0.6)
    while True:#кнопка dir
        r = pyautogui.locateOnScreen('dir.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
    time.sleep(0.6)
    pyautogui.write(dir_name)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    while True:#кнопка имя файла
        r = pyautogui.locateOnScreen('file_name.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
    time.sleep(0.6)
    pyautogui.write(file_nane)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(5)#пауза для прогрузки файла

def save_photo_close():
    pyautogui.hotkey('shift','f11')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)


def power_off():# выключение компа
    while True:#кнопка пуск
        r = pyautogui.locateOnScreen('start.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
    time.sleep(0.6)
    while True:#кнопка завершение работы
        r = pyautogui.locateOnScreen('power_off.png', grayscale=True, confidence=.9)
        if r is not None:
            e = pyautogui.center(r)
            pyautogui.leftClick(e)
            break
        else:
            r = None
    time.sleep(0.6)




















