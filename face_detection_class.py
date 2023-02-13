import face_recognition as fr
import pyautogui
import time

class FaceDetection:
    def __init__(self,path_to_reference)):
        self.open_reference_face = fr.load_image_file(path_to_reference)