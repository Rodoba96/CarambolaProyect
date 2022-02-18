#Apply a mask of the image showing only the desired color
#Obtain the contour of the object on mask image to btain the position of the object
#Draw a rectangle
#https://www.youtube.com/watch?v=cMJwqxskyek

import cv2
from cv2 import VideoCapture
import numpy as np
#import matplotlib.pyplot as plt

#Ranges for yellow H S    V(default)
lower = np.array([15, 100, 20])
upper = np.array([35, 255, 255])
#lower = np.array([0, 150, 20])
#upper = np.array([10, 255, 255])

#Video
cap = cv2.VideoCapture(0)


while True:

    ret,frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convert the image into HSV
    mask = cv2.inRange( image, lower, upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) !=0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),3)

    cv2.imshow('Mask', mask)
    cv2.imshow('webcam', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()