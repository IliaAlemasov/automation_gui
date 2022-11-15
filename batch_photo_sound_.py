import random

import pyautogui

from sound_setings import *
from def_for_PH_batch import *
import pyttsx3

if __name__ == '__main__':

    engine = pyttsx3.init()
    settings1_soud()

    engine.say("сколько фото обработать?")
    engine.runAndWait()
    print('сколько фото обрабоать?')

    xfoto = int(input())

    time.sleep(10)#пауза до старта

    pyautogui.FAILSAFE = True  # аварийное выключение

    fanny = ['если тебе конечно не пофиг','нужно же тебе на чем то учиться','в минуты сам переведешь',
             'может поработаем над оптимизацией?','может оперативки добавить?','как думаешь я достаточно хорош?',
             'что бы ты не думал что я только одно и то же могу болтать','а выходной на этой неделе у меня будет?',
             'здесь должна быть какая ни будь шутка','бла бла бля, ну в общем ты понял']

    for i in range(xfoto):
        s_time = time.time()#ниже блок кода для обработки
        copy_layer()
        ph_levels1()
        open_nik()
        target_filter1_nik()
        apply_nik()
        loading_pause()
        open_partiture()
        load_partiture()
        after_partiture25()
        loading_pause_short()
        #save_photo_close()
        time.sleep(5)
        e_time = time.time()# граница блока обработки
        p_time = round(e_time-s_time)
        p_t = str(p_time)
        r_fanny = random.choice(fanny)
        engine.say("сделал фотку, обработка заняла" + p_t + "секунд"+   r_fanny)
        engine.runAndWait()
    engine.say("Шеф все готово, не забудь подкинуть в топку новых фото")
    engine.runAndWait()
    print('шеф все готово!')

