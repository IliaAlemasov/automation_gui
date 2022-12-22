import pyautogui
import keyboard

"""EN This script measures the coordinates of the mouse pointer
on the screen and writes to logclick.txt file.
Measurement and recording are performed at the moment 
of pressing the key of the specified
on line 22. You can change the key to whatever you like.
The script is useful, for example, for measuring coordinates
buttons for pyautogui automation """

"""RU Этот скрипт измеряет координаты указателя мыши
на экране и записывает в файл logclick.txt .
Измерение и запись производятся в момент нажатия клавишы указанной
в строке 22. Вы можете поменять клавишу на любую удобную.
Скрипт полезен, например, для измерения координат
кнопок для pyautogui автоматизации"""

'''Думаю сделать нормальный оконный интерфейс на pyqt5.
Конечно надо будет разбираться с библиотеой и ООП заодно,
но в этом же и смысл?'''

if __name__ == '__main__':

    while True:
        keyboard.wait('Caps Lock')
        x, y = pyautogui.position()
        z = "{}".format(x)  # переводим в стороку
        v = "{}".format(y)
        # пишем в лог
        with open('logclick.txt', 'a') as log:
            log.write('x '+z + ','+'y '+v+'\n')



