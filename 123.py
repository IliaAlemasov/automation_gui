import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
image = cv2.imread('scr\\work_screenshot.jpeg')
location, vectors = hog.detectMultiScale(image, padding= (16,16), winStride= (2,2), scale= 1)
for (x, y, w, h) in location:

    cv2.rectangle(image, (x, y),

                  (x + w, y + h),

                  (0, 0, 255), 2)
cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()



