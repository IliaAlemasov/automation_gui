import os
from def_for_PH_batch_T2_second_PC import *

''' Этот срипт обрабатывает любое число фото: открывая, обрабатывая и сохраняя
по одной за раз. Обработку можно проводить по N разным алгоритмам, поместив фото
в папки с числовыми 1 2 3 и т.д. именами. Путь к папке должене быть только на EN,
 названия фото без кирилицы. Папку с именем, например "in_prodaction" необходимо
  поместить в корне любого диска, например E:\in_prodaction и подать на вход скрипта.
  '''

if __name__ == '__main__':
    print('укажите путь к папке')
    production_path = input('')
    print('обработка начнется через 10 секунд')
    time.sleep(10)

    adress_list = []  # список путей к папкам

    for adress, dirs, files in os.walk(production_path):
        adress_list.append(adress)

    adress_list.pop(0)  # удаляем путь к главной папке

    dir1 = adress_list[0]  # блок кода для папки 1

    for i in os.walk(dir1):
        pass
    name_files_list = i[-1]  # здесь список имен файлов в папке
    n_photo = len(name_files_list)  # длинна списка файлов для цикла for
    count = 0  # счетчик для for

    for o in range(n_photo):
        count += 1
        index = n_photo - count  # длинна списка - счетчик, получаем индекс для итерации
        file_name = name_files_list[index]  # получаем имя файла
        open_foto(dir1, file_name)  # далее алгоритм обработки
        delay_standart_medium()
        copy_layer()
        ph_levels1()
        copy_layer()
        delay_standart_medium()
        open_partiture()
        load_partiture()
        after_partiture25()
        loading_pause_short()
        copy_layer()
        open_nik()
        imported_but_nik()
        target_imported1_nik()
        apply_nik()
        loading_pause()
        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()

    dir2 = adress_list[1]  # блок кода для папки 2

    for i in os.walk(dir2):
        pass
    name_files_list = i[-1]  # здесь список имен файлов в папке
    n_photo = len(name_files_list)  # длинна списка файлов для цикла for
    count = 0  # счетчик для for

    for o in range(n_photo):
        count += 1
        index = n_photo - count  # длинна списка - счетчик, получаем индекс для итерации
        file_name = name_files_list[index]  # получаем имя файла
        open_foto(dir2, file_name)  # далее алгоритм обработки
        delay_standart_medium()
        copy_layer()
        open_partiture()
        load_partiture()
        after_partiture25()
        loading_pause_short()
        copy_layer()
        open_nik()
        imported_but_nik()
        target_imported1_nik()
        apply_nik()
        loading_pause()
        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()

    dir3 = adress_list[2]  # блок кода для папки 3

    for i in os.walk(dir3):
        pass
    name_files_list = i[-1]  # здесь список имен файлов в папке
    n_photo = len(name_files_list)  # длинна списка файлов для цикла for
    count = 0  # счетчик для for

    for o in range(n_photo):
        count += 1
        index = n_photo - count  # длинна списка - счетчик, получаем индекс для итерации
        file_name = name_files_list[index]  # получаем имя файла
        open_foto(dir3, file_name)  # далее алгоритм обработки
        delay_standart_medium()
        copy_layer()
        open_partiture()
        load_partiture()
        after_partiture25()
        loading_pause_short()
        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()

    dir4 = adress_list[3]  # блок кода для папки 4

    for i in os.walk(dir4):
        pass
    name_files_list = i[-1]  # здесь список имен файлов в папке
    n_photo = len(name_files_list)  # длинна списка файлов для цикла for
    count = 0  # счетчик для for

    for o in range(n_photo):
        count += 1
        index = n_photo - count  # длинна списка - счетчик, получаем индекс для итерации
        file_name = name_files_list[index]  # получаем имя файла
        open_foto(dir4, file_name)  # далее алгоритм обработки
        delay_standart_medium()
        open_partiture()
        load_partiture()
        after_partiture40()
        loading_pause_short()
        copy_layer()
        open_nik()
        imported_but_nik()
        target_imported1_nik()
        apply_nik()
        loading_pause()()
        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()

    dir5 = adress_list[4]  # блок кода для папки 5

    for i in os.walk(dir5):
        pass
    name_files_list = i[-1]  # здесь список имен файлов в папке
    n_photo = len(name_files_list)  # длинна списка файлов для цикла for
    count = 0  # счетчик для for

    for o in range(n_photo):
        count += 1
        index = n_photo - count  # длинна списка - счетчик, получаем индекс для итерации
        file_name = name_files_list[index]  # получаем имя файла
        open_foto(dir5, file_name)  # далее алгоритм обработки
        delay_standart_medium()
        copy_layer()
        ph_levels2()
        copy_layer()
        delay_standart_medium()
        open_partiture()
        load_partiture()
        after_partiture40()
        loading_pause_short()
        copy_layer()
        open_nik()
        imported_but_nik()
        target_imported1_nik()
        apply_nik()
        loading_pause()
        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()

    dir6 = adress_list[5]  # блок кода для папки 6

    for i in os.walk(dir6):
        pass
    name_files_list = i[-1]  # здесь список имен файлов в папке
    n_photo = len(name_files_list)  # длинна списка файлов для цикла for
    count = 0  # счетчик для for

    for o in range(n_photo):
        count += 1
        index = n_photo - count  # длинна списка - счетчик, получаем индекс для итерации
        file_name = name_files_list[index]  # получаем имя файла
        open_foto(dir6, file_name)  # далее алгоритм обработки
        copy_layer()
        open_nik()
        target_filter2_nik()
        apply_nik()
        loading_pause()
        open_partiture()
        load_partiture()
        after_partiture40()
        loading_pause_short()
        open_partiture()
        load_partiture()
        after_partiture25()
        loading_pause_short()
        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()

    power_off()
