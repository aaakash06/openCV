import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # _, thresh = cv2.threshold(gray, 0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # haar_cascade = cv2.CascadeClassifier('face.xml') 
    # faces_rect = haar_cascade.detectMultiScale( 
    # img, scaleFactor=1.1, minNeighbors=9) 
    
    # for (x, y, w, h) in faces_rect: 
    #       cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2) 
  
    cv2.imshow('Detected faces', img) 
    cv2.imshow('Detected faces', imgg) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    


