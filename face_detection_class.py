import face_recognition as fr
import pyautogui
import time


class FaceDetection:
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

        target_index = index_match_encoding[0]
        self.location_target_face = self.location_face_work_image[target_index]


    # Вычисляем координаты x,y для центра целевого лица и кликаем туда
    def click_on_center_target_face(self):
        y_centr_target_face = (self.location_target_face[0] + self.location_target_face[2]) / 2
        x_centr_target_face = (self.location_target_face[1] + self.location_target_face[3]) / 2
        pyautogui.moveTo(x_centr_target_face, y_centr_target_face)
        pyautogui.click()


