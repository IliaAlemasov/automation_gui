import pyautogui
import time
from def_for_PH_batch_T1_second_PC import delay_standart, delay_standart_medium, \
    check_button_on_screen, click_on_center_button, check_button_on_screen_on_for_short
import os
from def_for_PH_batch_T2_second_PC import open_foto, save_photo_close
import face_recognition as fr

eyes_size_l_point = 1238, 289
eyes_size_r_point = 1423, 289

eyes_height_l_point = 1238, 324
eyes_height_r_point = 1423, 324

''' PlasticFace -> Базовый класс для пластики с учетом лица в фотошоп.
                  Используеться, когда на фото гарантировано одно целевое лицо.
                  Включает в себя обработку ошибки, если движок пластики в фотошопе
                  не смог опредилить лицо. В таком случае обработка фото будет пропущена
                  Подходит для пакетной обработки с циклом for'''


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

    '''проверка на равенство аргумента 0 в этих методах не нужна, так как просто нет смысла
       запускать метод с 0 аргументом'''

    def wight_face(self, wight_face='0'):  # метод для ширины лица
        if self.bt0 is None:  # проверка наличие ошибки обнаружения лица в ФШ, аналогично для других методов
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

    def jaw_line(self, jaw_line='0'):  # метод для линии подбородка
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

    def chin_height(self, chin_height='0'):  # метод для высоты подбородка
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

    '''Здесь не придумал ничего лучше чем лесенка из if для проверки равенства аргумента 0
    С глазами все индивидумально - кому то нужен только 1 параметр, кому то все 4.
    Разбиение на 4 метода показались лишним усложнением'''


    def eyes_size_correction(self, eyes_size_l='0',  # метод для коррекции размера глаз
                             eyes_size_r='0', eyes_height_l='0', eyes_height_r='0'):
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

    def close_plastic(self):  # метод для закрытия палстики
        if self.bt0 is None:  # работает только если нет ошибки распознования лица в ФШ
            delay_standart()  # Если ошибка есть - просто пропускает этот блок
            pyautogui.press('enter')
            delay_standart_medium()


'''FaceDetectionAbstract -> Абстрактный класс для детекции лица - без привязки к конкретной реализации.
   Ну по крайней мере потытался выкинуть все нюансы реализации для пластики.
   Что бы была возможность переиспользовать если распознование лица по этой 
   технологии пригодится для чего то еще. Возможно потом будет нужно дополнить
   какими ни будь методами'''


class FaceDetectionAbstract:
    # Запускаем класс, передаем путь к образцу лица
    def __init__(self, path_to_reference=''):
        open_reference_face = fr.load_image_file(path_to_reference)
        self.reference_face_encoding = fr.face_encodings(open_reference_face)

    # делаем скриншот, получаем энкодинги и локации лиц
    def make_work_image(self):
        screenshot = pyautogui.screenshot()
        screenshot.save('scr/work_screenshot.jpeg')
        open_work_image = fr.load_image_file('scr/work_screenshot.jpeg')
        self.work_image_encoding = fr.face_encodings(open_work_image)
        self.location_face_work_image = fr.face_locations(open_work_image)

    # получаем кортеж с координатами целевого лица
    def get_location_target_face(self, for_tolerance_matching=0.5):
        index_match_encoding = []

        for index, work_encoding in enumerate(self.work_image_encoding):
            match_face = fr.compare_faces(self.reference_face_encoding, work_encoding,
                                          tolerance=for_tolerance_matching)
            if match_face == [True]:
                index_match_encoding.append(index)
                break
            else:
                pass
        try:
            target_index = index_match_encoding[0]
            self.location_target_face = self.location_face_work_image[target_index]
        except IndexError:  # Обработка ошибки при обращении по индексу к пустому списку
            self.location_target_face = None  # Присваиваем None что бы делать проверку в других методах
            print('Target face not fund! Please try change for_tolerance_matching')
            print(self.location_target_face)
            print(type(self.location_target_face))

    # адаптер для pyautogui.moveTo() - возвращает x,y целевого лица
    def adapter_for_pyautogui_move_to_x_y(self):
        if self.location_target_face is not None:
            self.y_centr_target_face = (self.location_target_face[0] + self.location_target_face[2]) / 2
            self.x_centr_target_face = (self.location_target_face[1] + self.location_target_face[3]) / 2
        else:
            pass


''' PlasticWithFaceDetection -> класс наследник FaceDetectionAbstract и PlasticFace
    Используется для пластики лиц в ШФ, когда на фото больше 1 человека
    И коррекцию надо сделать для 1 целевого лица
    Может рабоать и для фото с 1 персоной, но избыточен '''
class PlasticWithFaceDetection(FaceDetectionAbstract, PlasticFace):
    def __init__(self, path_to_reference=''):
        FaceDetectionAbstract.__init__(self, path_to_reference)

    def open_plastic(self):
        PlasticFace.__init__(self)

    # выбираем другой инструмент, что бы линии выделения лиц не попали на скриншот
    # И не мешали матчингу лиц, потом снова выбраем платику с учетом лиц,
    # что бы методы для пластики ФШ корректно работали
    def make_work_image_plastic(self):
        pyautogui.press('w')
        time.sleep(.5)
        pyautogui.moveTo(50, 50)
        FaceDetectionAbstract.make_work_image(self)
        time.sleep(.5)
        pyautogui.press('a')


    # Внутри метода запускается get_location_target_face и адаптер
    # Для того что бы сделать вызов в клиентком коде более высокоуровневым и понятным
    # Сам путался что надо запустить 3 метода без аргументов
    # что бы клинкуть в целевое лицо

    def click_on_center_target_face(self):
        FaceDetectionAbstract.get_location_target_face(self)
        FaceDetectionAbstract.adapter_for_pyautogui_move_to_x_y(self)
        if self.location_target_face is not None:
            pyautogui.moveTo(self.x_centr_target_face, self.y_centr_target_face)
            pyautogui.click()
        else:
            pass

    # для методов пластики доп проверка на на ошибку
    # распознования целевого лица через face recognition
    # Методы пластики будут выполнятся только если ее нет.
    # может случится ситуация когда FR лиц не нашел а ФШ нашел
    # Тогда лучше не делать ничего, чем похудить мужика или
    # применить параметры пластики к другому лицу
    def wight_face_with_detection(self, wight_face='0'):
        if self.location_target_face is not None:
            PlasticFace.wight_face(self, wight_face)
        else:
            pass

    def jaw_line_with_detection(self, jaw_line='0'):
        if self.location_target_face is not None:
            PlasticFace.jaw_line(self, jaw_line)
        else:
            pass

    def chin_height_with_detection(self, chin_height='0'):
        if self.location_target_face is not None:
            PlasticFace.chin_height(self, chin_height)
        else:
            pass

    def eyes_size_correction_with_detection(self, eyes_size_l='0', eyes_size_r='0',
                                            eyes_height_l='0', eyes_height_r='0'):
        if self.location_target_face is not None:
            PlasticFace.eyes_size_correction(self, eyes_size_l, eyes_size_r,
                                             eyes_height_l, eyes_height_r)
        else:
            pass
    # в метод закрытия пластики так же добавлен вариант
    # корректного закрытия если FR не нашел целевое лицо
    # а фш - лица увидел

    def close_plastic_with_detection(self):
        if self.location_target_face is not None:
            PlasticFace.close_plastic(self)
        else:
            pyautogui.click()
            time.sleep(.5)
            pyautogui.press("esc")
            time.sleep(.5)


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
        Elena = PlasticWithFaceDetection(path_to_reference='C:\\face_reference\\Tatayna1.jpg')
        Elena.open_plastic()
        Elena.make_work_image_plastic()
        Elena.click_on_center_target_face()
        Elena.wight_face_with_detection(wight_face='-10')
        Elena.jaw_line_with_detection(jaw_line='-50')
        Elena.eyes_size_correction_with_detection(eyes_size_l='10',
                                                  eyes_size_r='10', eyes_height_r='5', eyes_height_l= '5')
        Elena.chin_height_with_detection(chin_height='20')
        Elena.close_plastic_with_detection()

        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()


