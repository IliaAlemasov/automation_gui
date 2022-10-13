from def_for_PH_batch import *


if __name__ == '__main__':

    print('сколько фото обрабоать?')
    xfoto = int(input())

    time.sleep(10)#пауза до старта

    pyautogui.FAILSAFE = True  # аварийное выключение

    for u in range(xfoto):
        copy_layer()
        open_nik()
        custom_but_nik()
        target_filter1_nik()
        apply_nik()
        loading_pause()
        after_partiture40()
        pyautogui.press('f3')
        pyautogui.press('f2')
        loading_pause_short()
        open_nik()
        custom_but_nik()
        target_filter2_nik()
        apply_nik()
        loading_pause()
        #save_photo_close()
        time.sleep(5)
    print('шеф все готово!')








