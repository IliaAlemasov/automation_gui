import face_recognition as fr
import pyautogui
import time

def find_location_face_on_screen(path_to_reference = '', path_to_work_image = '', for_tolerance_matching = 0.3):
    open_reference_face = fr.load_image_file(path_to_reference)
    reference_face_encoding = fr.face_encodings(open_reference_face)

    open_work_image = fr.load_image_file(path_to_work_image)
    work_image_encoding = fr.face_encodings(open_work_image)
    location_face_work_image = fr.face_locations(open_work_image)

    index_match_encoding = []

    for index, work_encoding in enumerate(work_image_encoding):
        match_face = fr.compare_faces(reference_face_encoding, work_encoding, tolerance= for_tolerance_matching)
        if match_face == [True]:
            index_match_encoding.append(index)
            break
        else:
            pass

    target_index = index_match_encoding[0]
    return location_face_work_image[target_index]


#print(location_face)
time.sleep(10)
src = pyautogui.screenshot()
src.save('scr/work_screenshot.jpeg')
location_face = find_location_face_on_screen(path_to_reference = 'E:/face_model/Elena/Elena.jpg',
                                             path_to_work_image = 'scr/work_screenshot.jpeg',
                                             for_tolerance_matching = 0.3)

y_centr_target_face = (location_face[0] + location_face[2])/2
x_centr_target_face = (location_face[1] + location_face[3])/2
pyautogui.moveTo(x_centr_target_face,y_centr_target_face)
pyautogui.click()

