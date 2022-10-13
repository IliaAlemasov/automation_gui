import os
from def_for_PH_batch import *

''' не забудь поменять 3 значения y для каждого
    блока по индексу номер папки -1'''

print ('укажите путь к папке')
y = input('')
time.sleep(10)

adress_list=[]#список путей к папкам

for adress, dirs, files in os.walk(y):
    adress_list.append(adress)

adress_list.pop(0)#удаляем путь к главной папке

y1 = adress_list[0] #блок кода для папки 1

for i in os.walk(y1):
    pass
z = i[-1] #здесь список имен файлов в папке
n_photo = len(z) #длинна списка файлов для цикла for
count = 0 #счетчик для for

for o in range(n_photo):
    count += 1
    v = n_photo - count  # длинна списка - счетчик
    x = z[v]  # получаем индекс для итерации
    open_foto(y1, x)  # далее алгоритм обработки
    copy_layer()
    open_partiture()
    load_partiture()
    after_partiture40()
    open_nik()
    custom_but_nik()
    target_filter1_nik()
    apply_nik()
    loading_pause()
    save_photo_close()  # закрыть и сохранить
    time.sleep(3)

y2 = adress_list[1] #блок кода для папки 2

for i in os.walk(y2):
    pass
z = i[-1] #здесь список имен файлов в папке
n_photo = len(z) #длинна списка файлов для цикла for
count = 0 #счетчик для for

for o in range(n_photo):
    count += 1
    v = n_photo - count  # длинна списка - счетчик
    x = z[v]  # получаем индекс для итерации
    open_foto(y2, x)  # далее алгоритм обработки
    copy_layer()
    open_partiture()
    load_partiture()
    after_partiture25()
    open_nik()
    custom_but_nik()
    target_filter2_nik()
    apply_nik()
    loading_pause()
    color_correction1()
    loading_pause_short()
    save_photo_close()  # закрыть и сохранить
    time.sleep(3)

y3 = adress_list[2] #блок кода для папки 3

for i in os.walk(y3):
    pass
z = i[-1] #здесь список имен файлов в папке
n_photo = len(z) #длинна списка файлов для цикла for
count = 0 #счетчик для for

for o in range(n_photo):
    count += 1
    v = n_photo - count  # длинна списка - счетчик
    x = z[v]  # получаем индекс для итерации
    open_foto(y3, x)  # далее алгоритм обработки
    copy_layer()
    ph_levels1()
    open_partiture()
    load_partiture()
    after_partiture25()
    open_nik()
    custom_but_nik()
    target_filter3_nik()
    apply_nik()
    loading_pause()
    color_correction1()
    loading_pause_short()
    save_photo_close()  # закрыть и сохранить
    time.sleep(3)

y4 = adress_list[3] #блок кода для папки 4

for i in os.walk(y4):
    pass
z = i[-1] #здесь список имен файлов в папке
n_photo = len(z) #длинна списка файлов для цикла for
count = 0 #счетчик для for

for o in range(n_photo):
    count += 1
    v = n_photo - count  # длинна списка - счетчик
    x = z[v]  # получаем индекс для итерации
    open_foto(y4, x)  # далее алгоритм обработки
    copy_layer()
    ph_levels2()
    open_partiture()
    load_partiture()
    after_partiture25()
    open_nik()
    custom_but_nik()
    target_filter3_nik()
    apply_nik()
    loading_pause()
    color_correction2()
    loading_pause_short()
    save_photo_close()  # закрыть и сохранить
    time.sleep(3)

y5 = adress_list[4] #блок кода для папки 5

for i in os.walk(y5):
    pass
z = i[-1] #здесь список имен файлов в папке
n_photo = len(z) #длинна списка файлов для цикла for
count = 0 #счетчик для for

for o in range(n_photo):
    count += 1
    v = n_photo - count  # длинна списка - счетчик
    x = z[v]  # получаем индекс для итерации
    open_foto(y5, x)  # далее алгоритм обработки
    copy_layer()
    open_partiture()
    load_partiture()
    after_partiture25()
    open_nik()
    custom_but_nik()
    target_filter3_nik()
    apply_nik()
    loading_pause()
    color_correction2()
    loading_pause_short()
    save_photo_close()  # закрыть и сохранить
    time.sleep(3)

y6 = adress_list[5] #блок кода для папки 6

for i in os.walk(y6):
    pass
z = i[-1] #здесь список имен файлов в папке
n_photo = len(z) #длинна списка файлов для цикла for
count = 0 #счетчик для for

for o in range(n_photo):
    count += 1
    v = n_photo - count  # длинна списка - счетчик
    x = z[v]  # получаем индекс для итерации
    open_foto(y6, x)  # далее алгоритм обработки
    copy_layer()
    ph_levels1()
    open_partiture()
    load_partiture()
    after_partiture25()
    open_nik()
    custom_but_nik()
    target_filter3_nik()
    apply_nik()
    loading_pause()
    color_correction2()
    loading_pause_short()
    save_photo_close()  # закрыть и сохранить
    time.sleep(3)

power_off()

