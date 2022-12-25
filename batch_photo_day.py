from def_for_PH_batch_T2 import *

'''This script make production n_photo was opened in PH '''
'''Скрипт выполнит обработку  N-фото, уже открых внутри фотошопа по заданному 
в теле цикла алгоритму и сохранит результат с закриытием файлов'''

if __name__ == '__main__':

    print('сколько фото обрабоать?')
    n_photo = int(input())

    time.sleep(10)  # пауза до старта

    pyautogui.FAILSAFE = True  # аварийное выключение

    for u in range(n_photo):
        copy_layer()
        open_nik()
        custom_but_nik()
        target_filter1_nik()
        apply_nik()
        loading_pause()
        after_partiture40()
        loading_pause_short()
        open_nik()
        custom_but_nik()
        target_filter2_nik()
        apply_nik()
        loading_pause()
        save_photo_close()
        delay_standart_long()
    print('шеф все готово!')
