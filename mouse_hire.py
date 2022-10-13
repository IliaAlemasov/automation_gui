import pyautogui
import keyboard

while True:
    keyboard.wait('Caps Lock')
    x, y = pyautogui.position()
    z = "{}".format(x)  # переводим в стороку
    v = "{}".format(y)
    # пишем в лог
    log= open('logclick.txt','a')
    log.write('x '+z +','+'y '+v+'\n')
    log.close()
