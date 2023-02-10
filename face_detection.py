import cv2
import cmake
import dlib
import face_recognition

Elena = face_recognition.load_image_file('E:/face_model/Elena/Elena.jpg')
Elena_encoding = face_recognition.face_encodings(Elena)

work_image = face_recognition.load_image_file('E:/face_model/Elena/IMG_3780.jpg')
work_encoding = face_recognition.face_encodings(work_image)
find_face_work_images = face_recognition.face_locations(work_image)

for i in work_encoding:
    target_encoding =  face_recognition.compare_faces(Elena_encoding, i)
    print(target_encoding)






