import pyautogui
import time
from def_for_PH_batch_T1_second_PC import delay_standart, delay_standart_medium,\
    check_button_on_screen, click_on_center_button, check_button_on_screen_on_for_short
import os
from def_for_PH_batch_T2_second_PC import  open_foto, save_photo_close
from  face_detection_class import FaceDetection

eyes_size_l_point = 1238, 289
eyes_size_r_point = 1423, 289

eyes_height_l_point =1238, 324
eyes_height_r_point =1423, 324

class PlasticFace:
    def __init__(self):  # запускает пластику при запуске класса
        pyautogui.press('f2')
        delay_standart()
        pyautogui.hotkey('shift', 'ctrl', 'x')
        check_button_on_screen('buttons2pc\\check_plastic.png')
        delay_standart()
        pyautogui.press('a')
        # проверяет на ошибку распознания лиц в ФШ
        self.bt0 = check_button_on_screen_on_for_short('buttons2pc\\no_face.png')
        if self.bt0 is not None:
            delay_standart()
            pyautogui.press('enter')
            delay_standart()
            pyautogui.press('esc')
            delay_standart()
            # запоминаем есть ли ошибка распознования лиц в ФШ и
        # соотвествнно есть ли смысл для дальнейшего выполнения методов в этом цикле


    def wight_face(self, wight_face = '0'):  # метод для ширины лица
        if self.bt0 is None:
            pyautogui.moveTo(100, 100)
            bt1 = check_button_on_screen('buttons2pc\\width_face.png', for_confidence=.9)
            click_on_center_button(bt1)
            delay_standart()
            pyautogui.write(wight_face)
            delay_standart()
            pyautogui.press('enter')
            delay_standart()
        else:
            pass
        delay_standart()


    def jaw_line(self, jaw_line = '0'):  # метод для линии подбородка
        if self.bt0 is None:
            pyautogui.moveTo(100, 100)
            bt1 = check_button_on_screen('buttons2pc\\jaw_line.png', for_confidence=.9)
            click_on_center_button(bt1)
            delay_standart()
            pyautogui.write(jaw_line)
            delay_standart()
            pyautogui.press('enter')
            delay_standart()
        else:
            pass
        delay_standart()


    def chin_height(self, chin_height = '0'):  # метод для высоты подбородка
        if self.bt0 is None:
            pyautogui.moveTo(100, 100)
            bt1 = check_button_on_screen('buttons2pc\\chin_height.png', for_confidence=.9)
            click_on_center_button(bt1)
            delay_standart()
            pyautogui.write(chin_height)
            delay_standart()
            pyautogui.press('enter')
            delay_standart()
        else:
            pass
        delay_standart()


    def eyes_size_correction(self,eyes_size_l = '0', #  метод для коррекции размера глаз
                 eyes_size_r = '0', eyes_height_l = '0', eyes_height_r = '0'):
        if self.bt0 is None:
            if eyes_size_l != '0':
                pyautogui.moveTo(eyes_size_l_point)
                delay_standart()
                pyautogui.click()
                pyautogui.write(eyes_size_l)
                delay_standart()
                pyautogui.press('enter')
                delay_standart()
                if eyes_size_r != '0':
                    pyautogui.moveTo(eyes_size_r_point)
                    delay_standart()
                    pyautogui.click()
                    pyautogui.write(eyes_size_r)
                    delay_standart()
                    pyautogui.press('enter')
                    delay_standart()
                    if eyes_height_l != '0':
                        pyautogui.moveTo(eyes_height_l_point)
                        delay_standart()
                        pyautogui.click()
                        pyautogui.write(eyes_height_l)
                        delay_standart()
                        pyautogui.press('enter')
                        delay_standart()
                        if eyes_height_r != '0':
                            pyautogui.moveTo(eyes_height_r_point)
                            delay_standart()
                            pyautogui.click()
                            pyautogui.write(eyes_height_r)
                            delay_standart()
                            pyautogui.press('enter')
                            delay_standart()
            else:
                pass
        delay_standart()

    def close_plastic(self):
        if self.bt0 is None:
            delay_standart()
            pyautogui.press('enter')
            delay_standart_medium()


if __name__ == '__main__':
    print('укажите путь к папке')
    production_path = input('')
    print('обработка начнется через 10 секунд')
    time.sleep(10)

    face_Elena = FaceDetection(path_to_reference= 'C:\\face_reference\\Elena.jpg')

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
        Elena = PlasticFace()
        face_Elena.make_work_image()
        face_Elena.get_location_target_face()
        face_Elena.click_on_center_target_face()
        Elena.wight_face(wight_face='-30')
        Elena.jaw_line(jaw_line='-60')
        Elena.chin_height(chin_height='30')
        Elena.eyes_size_correction(eyes_size_l='30', eyes_size_r='50')
        Elena.close_plastic()
        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()








