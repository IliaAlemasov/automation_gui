import time
import pyautogui
from def_for_PH_batch_T1_second_PC import *

'''It library base value and functional def for easy and fast construction
 algorithms batch photo production '''

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
    bt = check_button_on_screen('buttons2pc\\por_icon.png', for_confidence=.7)
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
    bt = check_button_on_screen_on_for('buttons2pc\\update.png',
                                       for_confidence=.9)  # проверка на окно обновлений и его закрытие
    if bt is not None:
        pyautogui.press('Esc')
    else:
        pass


def custom_but_nik():  # кнопка custon nik
    bt = check_button_on_screen('buttons2pc\\custom.png', for_confidence=.99)
    click_on_center_button(bt)
    delay_standart()


def target_filter1_nik():  # кнопка target filter1
    bt = check_button_on_screen('buttons2pc\\custom1.png', for_confidence=.8)
    click_custom1(bt)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def target_filter2_nik():  # кнопка target filter2
    bt = check_button_on_screen('buttons2pc\\custom2.png', for_confidence=.8)
    click_custom1(bt)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def target_filter3_nik():  # кнопка target filter3
    bt = check_button_on_screen('buttons2pc\\custom3.png', for_confidence=.8)
    click_custom1(bt)
    delay_load_nik_preview()  # для прогрузки предпросмотра плагинов никон


def target_filter4_nik():  # кнопка target filter4
    bt = check_button_on_screen('buttons2pc\\custom4.png', for_confidence=.8)
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


def imported_but_nik():
    bt = check_button_on_screen('buttons2pc\\imported.png', for_confidence=.99)
    click_on_center_button(bt)
    delay_load_nik_preview()

def target_imported1_nik():
    bt = check_button_on_screen('buttons2pc\\imported1.png', for_confidence=.88)
    click_custom1(bt)
    delay_load_nik_preview()


def target_imported2_nik():
    bt = check_button_on_screen('buttons2pc\\imported2.png', for_confidence=.88)
    click_custom1(bt)
    delay_load_nik_preview()


def target_imported3_nik():
    while True:
        bt = check_button_on_screen_on_for_short('buttons2pc\\imported3.png', for_confidence=.88)
        if bt is None:  # если кнопки нет - скролим на 1 вниз
            pyautogui.moveTo(xy_for_mouse_scroll_nik)
            pyautogui.scroll(-1)
            continue  # идем в начало цикла и проверяем снова
        else:  # если кнопка есть - все путем
            click_custom1(bt)
            delay_standart()
            break
    delay_load_nik_preview()


def target_imported4_nik():
    while True:
        bt = check_button_on_screen_on_for_short('buttons2pc\\imported4.png', for_confidence=.85)
        if bt is None:  # если кнопки нет - скролим на 1 вниз
            pyautogui.moveTo(xy_for_mouse_scroll_nik)
            pyautogui.scroll(-1)
            continue  # идем в начало цикла и проверяем снова
        else:  # если кнопка есть - все путем
            click_custom1(bt)
            delay_standart()
            break
    delay_load_nik_preview()


def target_imported5_nik():
    while True:
        bt = check_button_on_screen_on_for_short('buttons2pc\\imported5.png', for_confidence=.88)
        if bt is None:  # если кнопки нет - скролим на 1 вниз
            pyautogui.moveTo(xy_for_mouse_scroll_nik)
            pyautogui.scroll(-1)
            continue  # идем в начало цикла и проверяем снова
        else:  # если кнопка есть - все путем
            click_custom1(bt)
            delay_standart()
            break
    delay_load_nik_preview()


def target_imported6_nik():
    while True:
        bt = check_button_on_screen_on_for_short('buttons2pc\\imported6.png', for_confidence=.84)
        if bt is None:  # если кнопки нет - скролим на 1 вниз
            pyautogui.moveTo(xy_for_mouse_scroll_nik)
            pyautogui.scroll(-1)
            continue  # идем в начало цикла и проверяем снова
        else:  # если кнопка есть - все путем
            click_custom1(bt)
            delay_standart()
            break
    delay_load_nik_preview()


def target_imported7_nik():
    while True:
        bt = check_button_on_screen_on_for_short('buttons2pc\\imported7.png', for_confidence=.88)
        if bt is None:  # если кнопки нет - скролим на 1 вниз
            pyautogui.moveTo(xy_for_mouse_scroll_nik)
            pyautogui.scroll(-1)
            continue  # идем в начало цикла и проверяем снова
        else:  # если кнопка есть - все путем
            click_custom1(bt)
            delay_standart()
            break
    delay_load_nik_preview()


def target_imported8_nik():
    while True:
        bt = check_button_on_screen_on_for_short('buttons2pc\\imported8.png', for_confidence=.88)
        if bt is None:  # если кнопки нет - скролим на 1 вниз
            pyautogui.moveTo(xy_for_mouse_scroll_nik)
            pyautogui.scroll(-1)
            continue  # идем в начало цикла и проверяем снова
        else:  # если кнопка есть - все путем
            click_custom1(bt)
            delay_standart()
            break
    delay_load_nik_preview()


def apply_nik():  # кнопка готово плагины никон
    bt = check_button_on_screen('buttons2pc\\apply.png', for_confidence=.95)
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
    bt1 = check_button_on_screen('buttons2pc\\file.png', for_confidence=.9)
    click_on_center_button(bt1)
    delay_drop_dawn_list()
    # кнопка open:
    bt2 = check_button_on_screen('buttons2pc\\open.png', for_confidence=.9)
    click_on_center_button(bt2)
    delay_drop_dawn_list()
    # кнопка dir:
    bt3 = check_button_on_screen('buttons2pc\\dir.png', for_confidence=.9)
    click_on_center_button(bt3)
    delay_drop_dawn_list()
    pyautogui.write(dir_name)  # пишем имя папки
    delay_standart()
    pyautogui.press('enter')
    delay_standart()
    # кнопка имя файла:
    bt4 = check_button_on_screen('buttons2pc\\file_name.png', for_confidence=.9)
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
    bt1 = check_button_on_screen('buttons2pc\\start.png', for_confidence=.9)
    click_on_center_button(bt1)
    delay_drop_dawn_list()
    # кнопка завершение работы:
    bt2 = check_button_on_screen('buttons2pc\\power_off.png', for_confidence=.9)
    click_on_center_button(bt2)
    delay_drop_dawn_list()


if __name__ == '__main__':
    print("it library")