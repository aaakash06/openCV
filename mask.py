import cv2
import numpy as np

def callback(x):
  pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)



while(1):
 ret, frame = cap.read()
 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 ilowH = cv2.getTrackbarPos('lowH', 'image')
 ihighH = cv2.getTrackbarPos('highH', 'image')
 ilowS = cv2.getTrackbarPos('lowS', 'image')
 ihighS = cv2.getTrackbarPos('highS', 'image')
 ilowV = cv2.getTrackbarPos('lowV', 'image')
 ihighV = cv2.getTrackbarPos('highV', 'image')
 lower_hsv = np.array([ilowH, ilowS, ilowV])
 higher_hsv = np.array([ihighH, ihighS, ihighV])
 mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
 final = cv2.bitwise_and(frame,frame, mask= mask)
 cv2.imshow('mask', mask)
 cv2.imshow('frame', frame)
 cv2.imshow('frame', final)

 if(cv2.waitKey(1) & 0xFF == ord('q')):
    break


cv2.destroyAllWindows()
cap.release()