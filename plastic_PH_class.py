import pyautogui
import time
from def_for_PH_batch_T1_second_PC import delay_standart, delay_standart_medium, \
    check_button_on_screen, click_on_center_button, check_button_on_screen_on_for_short
import os
from def_for_PH_batch_T2_second_PC import open_foto, save_photo_close
# Последняя версия данной библиотеки была выпущена 3 года назад. Кажется, как будто её перестали поддерживать. Возможно стоит поискать что-то ещё.
# Знаю точно, что в OpenCv есть такая возможность, но насколько хорошо эти библиотеки работают - не знаю.
import face_recognition as fr

eyes_size_l_point = 1238, 289
eyes_size_r_point = 1423, 289

eyes_height_l_point = 1238, 324
eyes_height_r_point = 1423, 324

''' PlasticFace -> Базовый класс для пластики с учетом лица в фотошоп.
                  Используется, когда на фото гарантировано одно целевое лицо.
                  Включает в себя обработку ошибки, если движок пластики в фотошопе
                  не смог определить лицо. В таком случае обработка фото будет пропущена
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
        # соотвествено есть ли смысл для дальнейшего выполнения методов в этом цикле

    '''проверка на равенство аргумента 0 в этих методах не нужна, так как просто нет смысла
       запускать метод с 0 аргументом'''

    #функция шаблон для класа пластики: Проверяет на ошибку распознования лица ФШ,
    #Находит нужную кнопку по избражению и впечатывает параметр и другие важные мелочи
    def _check_err_check_bt_enter_param (self, bt_src: str, param : int):
        if self.bt0 is None:
            pyautogui.moveTo(100, 100)
            bt1 = check_button_on_screen(f'buttons2pc\\{bt_src}.png', for_confidence=.9)
            click_on_center_button(bt1)
            delay_standart()
            pyautogui.write(str(param))
            delay_standart()
            pyautogui.press('enter')
            delay_standart()

    # ширина по-английски - width
    # по-хорошему, такие параметры как wight_face передавать не как str, а как int, а потом уже где надо делать преобразование int -> str
    # Ещё один момент. Желательно в название функции добавить глагол - так проще будет понять, что делает эта функция.
    # Вот например, смотрю на функцию width_face - ширина лица. Ну и что эта функция делает с шириной лица? Мне не совсем понятно
    # Можно например так обозвать: correct_face_width (p.s. главное слово в словосочетании - это ширина,
    # а главное слово в англ. языке ставится в конце)
    def wight_face_correction(self, width_face='0'):  # метод для ширины лица
        self._check_err_check_bt_enter_param('width_face', int(width_face))
        # if self.bt0 is None:  # проверка наличие ошибки обнаружения лица в ФШ, аналогично для других методов
        #     pyautogui.moveTo(100, 100)
        #     bt1 = check_button_on_screen('buttons2pc\\width_face.png', for_confidence=.9)
        #     click_on_center_button(bt1)
        #     delay_standart()
        #     pyautogui.write(wight_face)
        #     delay_standart()
        #     pyautogui.press('enter')
        #     delay_standart()
        # else:
        #     pass
        # delay_standart()

    def jaw_line_correction(self, jaw_line='0'):  # метод для линии подбородка
        self._check_err_check_bt_enter_param('jaw_line', int(jaw_line))
        # if self.bt0 is None:
        #     pyautogui.moveTo(100, 100)
        #     bt1 = check_button_on_screen('buttons2pc\\jaw_line.png', for_confidence=.9)
        #     click_on_center_button(bt1)
        #     delay_standart()
        #     pyautogui.write(jaw_line)
        #     delay_standart()
        #     pyautogui.press('enter')
        #     delay_standart()
        # else:
        #     pass
        # delay_standart()

    def chin_height_correction(self, chin_height='0'):  # метод для высоты подбородка
        self._check_err_check_bt_enter_param('chin_height', int(chin_height))
        # if self.bt0 is None:
        #     pyautogui.moveTo(100, 100)
        #     bt1 = check_button_on_screen('buttons2pc\\chin_height.png', for_confidence=.9)
        #     click_on_center_button(bt1)
        #     delay_standart()
        #     pyautogui.write(chin_height)
        #     delay_standart()
        #     pyautogui.press('enter')
        #     delay_standart()
        # else:
        #     pass
        # delay_standart()

    '''Здесь не придумал ничего лучше чем лесенка из if для проверки равенства аргумента 0
    С глазами все индивидумально - кому то нужен только 1 параметр, кому то все 4.
    Разбиение на 4 метода показались лишним усложнением'''

    # Эти параметры лучше также изначально передавать как int
    def eyes_size_correction(self, eyes_size_l='0',  # метод для коррекции размера глаз
                             eyes_size_r='0', eyes_height_l='0', eyes_height_r='0'):
        if self.bt0 is  None:

            # данная функция будет видна только внутри функции eyes_size_correction. Если она нужна будет где-то ещё, можно вынести её в класс
            def func (point: tuple[int, int], size: int):
                pyautogui.moveTo(point)
                delay_standart()
                pyautogui.click()
                pyautogui.write(str(size))
                delay_standart()
                pyautogui.press('enter')
                delay_standart()

            # вот так, например, можно избавиться от лесенки из ифов
            eyes_values = [
                (eyes_size_l_point, eyes_size_l),
                (eyes_size_r_point, eyes_size_r),
                (eyes_height_l_point, eyes_height_l),
                (eyes_height_r_point, eyes_height_r),
            ]
            for eye_value in eyes_values:
                # если первое условие не выполнилось, то мы тупо выходим из цикла, и остальные условия проверяться даже и не будут
                if eye_value[1] == '0':
                    continue  # По логике работы если eye_value==0, этот параметр пропускаем, но дальше проверять надо.
                func(*eye_value) # это эквивалентно записи func(value[0], value[1], ..., value[n]). Таким же образом можно распаковывать не только кортежи, но и, например, списки
            delay_standart()

        # hint: для того, чтобы закомментировать несколько выделенных строк, нажми Ctrl + /
        # if eyes_size_l != '0':
        #     pyautogui.moveTo(eyes_size_l_point)
        #     delay_standart()
        #     pyautogui.click()
        #     pyautogui.write(eyes_size_l)
        #     delay_standart()
        #     pyautogui.press('enter')
        #     delay_standart()
        #     if eyes_size_r != '0':
        #         pyautogui.moveTo(eyes_size_r_point)
        #         delay_standart()
        #         pyautogui.click()
        #         pyautogui.write(eyes_size_r)
        #         delay_standart()
        #         pyautogui.press('enter')
        #         delay_standart()
        #         if eyes_height_l != '0':
        #             pyautogui.moveTo(eyes_height_l_point)
        #             delay_standart()
        #             pyautogui.click()
        #             pyautogui.write(eyes_height_l)
        #             delay_standart()
        #             pyautogui.press('enter')
        #             delay_standart()
        #             if eyes_height_r != '0':
        #                 pyautogui.moveTo(eyes_height_r_point)
        #                 delay_standart()
        #                 pyautogui.click()
        #                 pyautogui.write(eyes_height_r)
        #                 delay_standart()
        #                 pyautogui.press('enter')
        #                 delay_standart()
        # delay_standart()

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

    # адаптер для pyautogui.moveTo() - возвращает x,y целевого лица
    def adapter_for_pyautogui_move_to_x_y(self):
        if self.location_target_face is not None:
            self.y_centr_target_face = (self.location_target_face[0] + self.location_target_face[2]) / 2
            self.x_centr_target_face = (self.location_target_face[1] + self.location_target_face[3]) / 2
        else:
            pass

# множественное наследование не самая хорошая штука, лучше стараться его избегать, но в учебных целях можно
''' PlasticWithFaceDetection -> класс наследник FaceDetectionAbstract и PlasticFace
    Используется для пластики лиц в ШФ, когда на фото больше 1 человека
    И коррекцию надо сделать для 1 целевого лица
    Может рабоать и для фото с 1 персоной, но избыточен '''
class PlasticWithFaceDetection(FaceDetectionAbstract, PlasticFace):
    def __init__(self, path_to_reference=''):
        FaceDetectionAbstract.__init__(self, path_to_reference)
        PlasticFace.__init__(self)
    # инициализацию конструктора PlasticFace лучше также вынести в конструктор производного класса
    def open_plastic(self):
        PlasticFace.__init__(self)

    # выбираем другой инструмент, что бы линии выделения лиц не попали на скриншот
    # И не мешали матчингу лиц, потом снова выбраем платику с учетом лиц,
    # что бы методы для пластики ФШ корректно работали
    def make_work_image(self):
        # нужно именно переопределять (override) функцию базового класса, а не давать в производном классе похожее название
        # с помощью переопределения достигается так называемый полиморфизм. Попробую объяснить ниже
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
    def wight_face_correction(self, width_face='0'):
        # изменил название
        if self.location_target_face is not None:
            PlasticFace.wight_face_correction(self, width_face)
        else:
            pass

    def jaw_line_correction(self, jaw_line='0'):
        # изменил название
        if self.location_target_face is not None:
            PlasticFace.jaw_line_correction(self, jaw_line)
        # вообще здесь и во многих других случаях else -> pass не обязателен, можно (а может даже лучше) его убрать
        else:
            pass

    def chin_height_correction(self, chin_height='0'):
        # изменил название
        if self.location_target_face is not None:
            PlasticFace.chin_height_correction(self, chin_height)
        else:
            pass

    def eyes_size_correction(self, eyes_size_l='0', eyes_size_r='0',
                                            eyes_height_l='0', eyes_height_r='0'):
        # изменил название
        if self.location_target_face is not None:
            PlasticFace.eyes_size_correction(self, eyes_size_l, eyes_size_r,
                                             eyes_height_l, eyes_height_r)
        else:
            pass
    # в метод закрытия пластики так же добавлен вариант
    # корректного закрытия если FR не нашел целевое лицо
    # а фш - лица увидел

    def close_plastic(self):
        if self.location_target_face is not None:
            PlasticFace.close_plastic(self)
        else:
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

    # принципиально важно итерироваться по файлам с конца? Если нет, то я бы цикл сделал примерно так:
    # for photo in name_files_list:
    #     open_foto(dir1, photo)
    #     ...
    # в таком случае можно будет отказаться от переменных o, n_photo, count.
    # Тем более переменная o не используется (и между прочем может использоваться вместо count при твоей записи цикла)
    for o in range(n_photo):
        count += 1
        index = n_photo - count  # длинна списка - счетчик, получаем индекс для итерации
        file_name = name_files_list[index]  # получаем имя файла
        open_foto(dir1, file_name)  # далее алгоритм обработки
        delay_standart_medium()
        Elena = PlasticWithFaceDetection(path_to_reference='C:\\face_reference\\Elena.jpg')
        Elena.open_plastic()
        Elena.make_work_image()
        Elena.click_on_center_target_face()
        Elena.wight_face_correction(wight_face='-30')
        Elena.jaw_line_correction(jaw_line='-60')
        Elena.eyes_size_correction(eyes_size_l='30',
                                                  eyes_size_r=' 30')
        Elena.chin_height_correction(chin_height='20')
        Elena.close_plastic()

        save_photo_close()  # закрыть и сохранить
        delay_standart_medium()

'''
Почему надо именно переопределять функции, а не писать новые с похожим названием?
Рассмотрим класс животных. Все животные так или иначе умеют говорить

class Animal:
    def __init__ (self, name):
        self._name = name
    
    def say(word):
        ничего не делаем
        данный метод можно указать абстрактным (добавить декоратор @abstractmethod, кажется)
        
Теперь производные классы:
class Cat(Animal):
    def say_like_cat (word):
        говорим Мяу
        
class Dog(Animal):
    def say_like_dog (word):
        говорим Гав
        
А теперь организуем зоопарк и заставим их всех говорить:

animals = [Cat("Барсик"), Dog("Бобик"), Cat("Мурзик"),  Bird("Кеша")]
animals[0].say_like_cat("")
animals[1].say_like_dog("")
animals[2].say_like_cat("")
animals[3].say_like_bird("")

Вот только так их можно заставить говорить, по-другому никак, ведь у каждого класса свой метод отвечающий за разговор.
Приходится знать какой тип данных соответствует каждому элементу списка animals. А если этих элементов тысячи? 
Да, можно сделать проверку типов в цикле, но это так себе затея. Если типов будет много (читай у тебя будет много видов 
в твоем зоопарке и каждому виду будет соответствовать какой-нибудь класс), то можно будет застрелиться. 
Но при этом у всех у них есть функция say которая делает... ничего! Теперь реализуем классы по другому

class Cat(Animal):
    def say (word):
        говорим Мяу
        
class Dog(Animal):
    def say (word):
        говорим Гав

Теперь мы можем заставить твой зоопарк говорить вот таким образом:

for animal in animals:
    animal.say("something")

И нам вообще фиолетово, сколько у нас элементов в списке, сколько у нас видов животных (== реализаций класса Animal).
Это в двух словах о том, что такое полиморфизм. 

'''