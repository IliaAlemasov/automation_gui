import time
import pyautogui

# -----base def & value XY for construction tier 1 -----


def delay_before_click():  # пауза перед кликом
    time.sleep(0.1)


def delay_drop_dawn_list():  # пауза для раскрытия выпадающих списков
    time.sleep(.55)


def delay_load_partiture():  # пауза для загрузки партрируты
    time.sleep(7)


def delay_load_nik_preview():  # для прогрузки предпросмотра плагинов никон
    time.sleep(8)


def delay_standart():
    time.sleep(.5)


def delay_standart_medium():
    time.sleep(3)


def delay_standart_long():
    time.sleep(5)


def loading_pause():  # пауза для прогрузки очень долгих операций
    time.sleep(25)


def loading_pause_short():  # пауза для прогрузки долгих операций
    time.sleep(6)


def check_button_on_screen(button_path: str, for_grayscale=True, for_confidence=.9):
    while True:
        button = pyautogui.locateOnScreen(button_path, grayscale=for_grayscale, confidence=for_confidence)
        if button is not None:
            return (button)
        else:
            pass
        time.sleep(.7)  # пауза для оптимизации While


def check_button_on_screen_single(button_path: str, for_grayscale=True, for_confidence=.9):
    button = pyautogui.locateOnScreen(button_path, grayscale=for_grayscale, confidence=for_confidence)
    if button is not None:
        return (button)
    else:
        pass
    delay_standart()


def check_button_on_screen_on_for(button_path: str, for_grayscale=True, for_confidence=.9):
    for i in range(30):
        button = pyautogui.locateOnScreen(button_path, grayscale=for_grayscale, confidence=for_confidence)
        if button is not None:
            return (button)
        else:
            pass
        time.sleep(.7)  # пауза для оптимизации for


def click_on_center_button(button_box):
    center_button = pyautogui.center(button_box)
    pyautogui.leftClick(center_button)


def click_custom1(button_box):
    center_button = pyautogui.center(button_box)
    pyautogui.moveTo(center_button)
    delay_before_click()
    pyautogui.moveRel(0, -70)
    delay_before_click()
    pyautogui.leftClick()


xy_open_partiture1 = (871, 24)  # координаты кнопок для открытия partiture
xy_open_partiture2 = (1147, 870)
xy_open_partiture3 = (1533, 878)

xy_open_nik1 = (871, 24)  # координаты кнопок для открытия nik
xy_open_nik2 = (927, 918)
xy_open_nik3 = (1591, 916)
xy_open_nik4 = (1587, 948)