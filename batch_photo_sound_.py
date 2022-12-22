import random
from sound_setings import *
from def_for_PH_batch import *
import pyttsx3


'''This script make production n_photo was opened in PH.'''
'''Скрипт выполнит обработку  N-фото, уже открых внутри фотошопа по заданному 
в теле цикла алгоритму и сохранит результат с закриытием файлов. А так же развлечет
вас шутками и посчитает время обработки каждого фото в секундах.'''

if __name__ == '__main__':

    engine = pyttsx3.init()  # звуковой движок используется в развлекательно-обучающих целях
    settings2_sound()
    engine.say("сколько фото обработать?")
    engine.runAndWait()
    print('сколько фото обработать?')
    n_photo = int(input())
    time.sleep(10)  # пауза до старта

    pyautogui.FAILSAFE = True  # аварийное выключение

    # список с шутками так же для обучения/развлечения
    fanny = ['если тебе конечно не пофиг', 'нужно же тебе на чем то учиться', 'в минуты сам переведешь',
             'может поработаем над оптимизацией?', 'может оперативки добавить?', 'как думаешь я достаточно хорош?',
             'что бы ты не думал что я только одно и то же могу болтать', 'а выходной на этой неделе у меня будет?',
             'здесь должна быть какая ни будь шутка', 'бла бла бля, ну в общем ты понял']

    for i in range(n_photo):
        start_time = time.time()  # ниже блок кода для обработки
        copy_layer()
        ph_levels1()
        copy_layer()
        open_partiture()
        load_partiture()
        after_partiture25()
        open_nik()
        custom_but_nik()
        target_filter1_nik()
        apply_nik()
        loading_pause()
        save_photo_close()
        delay_standart_long()
        end_time = time.time()  # граница блока обработки
        production_time = round(end_time - start_time)
        production_time_str = str(production_time)
        random_fanny = random.choice(fanny)
        engine.say("сделал фотку, обработка заняла" + production_time_str + "секунд" + random_fanny)
        engine.runAndWait()
    engine.say("Шеф все готово, не забудь подкинуть в топку новых фото")
    engine.runAndWait()
    print('шеф все готово!')
