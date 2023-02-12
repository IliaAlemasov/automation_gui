
import face_recognition as fr
import os


#загружаем образец лица - возвращяет нампи массив
Elena = fr.load_image_file('E:/face_model/Elena/Elena.jpg')
#получаем вектор лица тип список
Elena_encoding = fr.face_encodings(Elena)

#загружаем рабочее фото - возвращает нампи массив
work_image = fr.load_image_file('E:/face_model/Elena/IMG_3930.jpg')
#получаем вектора лиц тип список
work_encoding = fr.face_encodings(work_image)
#получаем локации лиц, позващает список кортежей
find_face_work_images = fr.face_locations(work_image)
#print(find_face_work_images)
#print(type(find_face_work_images))

target_encoding = []

for index, var in enumerate(work_encoding):
   b = fr.compare_faces(Elena_encoding, var, tolerance=0.3)
   if b == [True]:
       target_encoding.append(index)
       break
   else:
       pass

target_index = target_encoding[0]
print(find_face_work_images[target_index])












