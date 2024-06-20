import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("car.jpg")
cv2.imshow("img", img)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

plt.imshow(hist)
highhsv = [90,146,255]
lowhsv = [10,0,255]
mask = cv2.inRange(hsv,np.array(lowhsv), np.array(highhsv))
# cv2.imshow("hist",hist)
cv2.imshow("mask",mask)
plt.show()
while True: 
  button = cv2.waitKey(0)
  if(button):
    break