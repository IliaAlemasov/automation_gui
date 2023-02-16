import face_recognition as fr
import pyautogui
import time


class FaceDetectionAbstract:
    #Запускаем класс, передаем путь к образцу лица
    def __init__(self,path_to_reference= ''):
        open_reference_face = fr.load_image_file(path_to_reference)
        self.reference_face_encoding = fr.face_encodings(open_reference_face)


    #делаем скриншот, получаем энкодинги и локации лиц
    def make_work_image(self):
        screenshot = pyautogui.screenshot()
        screenshot.save('scr/work_screenshot.jpeg')
        open_work_image = fr.load_image_file('scr/work_screenshot.jpeg')
        self.work_image_encoding = fr.face_encodings(open_work_image)
        self.location_face_work_image = fr.face_locations(open_work_image)



    # получаем кортеж с координатами целевого лица
    def get_location_target_face(self, for_tolerance_matching = 0.5):
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
        except IndexError:
            self.location_target_face = None
            print('Target face not fund! Please try change for_tolerance_matching')


    # адаптер для pyautogui.moveTo() - возвращает x,y целевого лица
    def adapter_for_pyautogui_move_to_x_y(self):
        if self.location_target_face is not None:
            y_centr_target_face = (self.location_target_face[0] + self.location_target_face[2]) / 2
            x_centr_target_face = (self.location_target_face[1] + self.location_target_face[3]) / 2
            return (x_centr_target_face,y_centr_target_face)


# Класс с нюансами реализации именно для палстики в фотошоп
class FaceDetectionForPlastic(FaceDetectionAbstract):
    # выбираем другой инструмент, что бы линии выделения лиц не попали на скриншот
    def make_work_image_plastic(self):
        pyautogui.press('w')
        time.sleep(.5)
        FaceDetectionAbstract.make_work_image()
        time.sleep(.5)
        pyautogui.press('a')



