import os
from def_for_PH_batch import *


if __name__ == '__main__':

    pyautogui.FAILSAFE = True  # аварийное выключение

    print ('укажите путь к папке')
    y = input('')
    time.sleep(6)
    for i in os.walk(y):
       pass
    z = i[-1] #здесь список имен файлов в папке
    n_photo = len(z) #длинна списка файлов для цикла for
    count = 0 #счетчик для for

    for o in range(n_photo):
        count += 1
        v = n_photo - count #длинна списка - счетчик
        x = z[v] # получаем индекс для итерации
        open_foto(y,x)#далее алгоритм обработки
        pyautogui.press('f2')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','i')
        time.sleep(0.5)
        save_photo_close()#закрыть и сохранить
        time.sleep(3)







