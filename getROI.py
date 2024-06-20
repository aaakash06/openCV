import cv2
import numpy as np
import matplotlib.pyplot as plt

def retrieveArea(event,x,y,a,b):
    if event == cv2.EVENT_LBUTTONDOWN:
        shift = 200
        roi = img[y-shift:y+shift, x-shift:x+shift]
        cv2.imshow("roi",roi)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv",hsv)


img = cv2.imread("car.jpg")
cv2.imshow("car_normal",img)


# while True:
#   cv2.setMouseCallback("car_normal",retrieveArea)
#   button = cv2.waitKey(0)
#   if(button):
#     break

cv2.setMouseCallback("car_normal",retrieveArea)
cv2.waitKey(0)
cv2.destroyAllWindows()