import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
image = cv2.imread('scr\\work_screenshot.jpeg')
location, = hog.detectMultiScale(image)
print((type(location)))
print(location)



