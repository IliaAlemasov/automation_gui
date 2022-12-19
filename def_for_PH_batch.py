import time
import pyautogui


# -----base def & value XY for constration tier 1 -----
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
    time.sleep(18)


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


# -----functional def tier 2-----#

def open_partiture():  # запуск партируры
    pyautogui.moveTo(xy_open_partiture1)
    delay_before_click()
    pyautogui.leftClick()
    delay_drop_dawn_list()
    pyautogui.moveTo(xy_open_partiture2)
    delay_drop_dawn_list()
    pyautogui.moveTo(xy_open_partiture3)
    delay_drop_dawn_list()
    pyautogui.leftClick()


def load_partiture():  # проверка на загрузку партритуры
    bt = check_button_on_screen('buttons\\por_icon.png', for_confidence=.7)
    if bt is not None:
        pyautogui.press('Enter')
    delay_load_partiture()


def after_partiture25():  # 25%
    pyautogui.hotkey('shift', 'ctrl', 'f12')
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    pyautogui.press('f3')
    delay_standart()
    pyautogui.press('f2')
    delay_standart()


def after_partiture40():  # 40%
    pyautogui.press('f11')
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    pyautogui.press('f3')
    delay_standart()
    pyautogui.press('f2')
    delay_standart()


def open_nik():  # запуск плагинов никон
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
    delay_standart_medium()  # пауза для загрузки окна плагинов
    bt = check_button_on_screen_on_for('buttons\\update.png',
                                       for_confidence=.9)  # проверка на окно обновлений и его закрытие
    if bt is not None:
        pyautogui.press('Esc')
    else:
        pass


def custom_but_nik():  # кнопка custon nik
    bt = check_button_on_screen('buttons\\custom.png', for_confidence=.99)
    click_on_center_button(bt)
    delay_standart()


def target_filter1_nik():  # кнопка target filter1
    bt = check_button_on_screen('buttons\\custom1.png', for_confidence=.8)
    click_custom1(bt)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def target_filter2_nik():  # кнопка target filter2
    bt = check_button_on_screen('buttons\\custom2.png', for_confidence=.8)
    click_custom1(bt)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def target_filter3_nik():  # кнопка target filter3
    bt = check_button_on_screen('buttons\\custom3.png', for_confidence=.8)
    click_custom1(bt)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def target_filter4_nik():  # кнопка target filter4
    bt = check_button_on_screen('buttons\\custom4.png', for_confidence=.8)
    click_custom1(bt)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def target_filter5_nik():  # кнопка target filter5 + избраное. Реализация для 4к
    for i in range(5):
        bt1 = check_button_on_screen_single('buttons\\star.png', for_grayscale=False, for_confidence=.95)
        if bt1 is not None:
            click_on_center_button(bt1)
            break
        else:
            pass
        delay_standart()
    bt2 = check_button_on_screen('buttons\\custom5.png', for_confidence=.8)
    click_custom1(bt2)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def apply_nik():  # кнопка готово плагины никон
    bt = check_button_on_screen('buttons\\apply.png', for_confidence=.95)
    click_on_center_button(bt)
    delay_standart()


def ph_levels1():  # уровни стандарт 248,1.04,1
    pyautogui.press('f2')
    delay_standart()
    pyautogui.hotkey('ctrl', 'f12')
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    pyautogui.press('f2')
    delay_standart()


def ph_levels2():  # уровни + 245,1.06,1
    pyautogui.press('f2')
    delay_standart()
    pyautogui.hotkey('shift', 'f12')
    delay_standart()
    pyautogui.press('f2')
    delay_standart()


def ph_levels3():  # уровни средние тона+ 1.1
    pyautogui.press('f2')
    delay_standart()
    pyautogui.hotkey('ctrl', 'f11')
    delay_standart()
    pyautogui.press('f2')
    delay_standart()


def copy_layer():
    pyautogui.press('f2')
    pyautogui.press('f2')


def color_correction1():
    pyautogui.press('f8')
    delay_standart()
    pyautogui.press('enter')


def color_correction2():
    pyautogui.hotkey('shift', 'f8')
    delay_standart()
    pyautogui.press('enter')


def open_foto(dir_name, file_nane):  # y это путь к папке строкой, x - имя файла
    # кнопка файл:
    bt1 = check_button_on_screen('buttons\\file.png', for_confidence=.9)
    click_on_center_button(bt1)
    delay_drop_dawn_list()
    # кнопка open:
    bt2 = check_button_on_screen('buttons\\open.png', for_confidence=.9)
    click_on_center_button(bt2)
    delay_drop_dawn_list()
    # кнопка dir:
    bt3 = check_button_on_screen('buttons\\dir.png', for_confidence=.9)
    click_on_center_button(bt3)
    delay_drop_dawn_list()
    pyautogui.write(dir_name)  # пишем имя папки
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    # кнопка имя файла:
    bt4 = check_button_on_screen('buttons\\file_name.png', for_confidence=.9)
    click_on_center_button(bt4)
    delay_standart()
    pyautogui.write(file_nane)  # пишем имя файла
    delay_standart()
    pyautogui.press('enter')
    delay_standart_long()  # пауза для прогрузки файла


def save_photo_close():
    pyautogui.hotkey('shift', 'f11')
    delay_standart()
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    delay_standart()


def power_off():  # выключение компа
    # кнопка пуск:
    bt1 = check_button_on_screen('buttons\\start.png', for_confidence=.9)
    click_on_center_button(bt1)
    delay_drop_dawn_list()
    # кнопка завершение работы:
    bt2 = check_button_on_screen('buttons\\power_off.png', for_confidence=.9)
    click_on_center_button(bt2)
    delay_drop_dawn_list()


if __name__ == '__main__':
    print("it library")
