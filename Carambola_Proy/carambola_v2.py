#Referencias:
# https://www.youtube.com/watch?v=cMJwqxskyek
# https://www.youtube.com/watch?v=nty0zSKB4_k

import cv2
from cv2 import VideoCapture
import numpy as np

#Ranges for yellow H   S   V(default)
lower_yellow = np.array([20, 80, 20])
upper_yellow = np.array([30, 255, 255])

#RED
lower_red = np.array([170, 150, 20])
upper_red = np.array([180, 255, 255])

#White 
lower_white = np.array([0, 0, 11])
upper_white = np.array([26, 82, 2])

#Imagenes
frame = cv2.imread('D:\Documentos\MisProyectos\CarambolaProyect\Carambola_Proy\imagenes\muestra_05.jpeg')

#Video
#cap = cv2.VideoCapture(0)


while True:

    #ret,frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convert the image into HSV
    #image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convert the image into HSV
    
    mask1 = cv2.inRange(image, lower_yellow, upper_yellow)
    mask2 = cv2.inRange(image, lower_red, upper_red)
    mask3 = cv2.inRange(image, lower_white, upper_white)

    contours1, hierarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours3, hierarchy = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    if len(contours1) !=0:
        #Yellow contours
        for i in contours1:
            if cv2.contourArea(i) < 638 and cv2.contourArea(i) > 360 :
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,255),3)
                #cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                center_x = x+(w//2)
                center_y = y+(h//2)
                cv2.circle(frame,(center_x,center_y),3,(255,0,255),-1)
                #cv2.circle(img,(center_x,center_y),3,(255,0,255),-1)
        #Red contours
        for i in contours2:
            if cv2.contourArea(i) > 500:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),3)
                #cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                center_x = x+(w//2)
                center_y = y+(h//2)
                cv2.circle(frame,(center_x,center_y),3,(255,0,255),-1)
                #cv2.circle(img,(center_x,center_y),3,(255,0,255),-1)
        #White contours
        for i in contours3:
            if cv2.contourArea(i) > 360:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(255,255,255),3)
                #cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                center_x = x+(w//2)
                center_y = y+(h//2)
                cv2.circle(frame,(center_x,center_y),3,(255,0,255),-1)
                #cv2.circle(img,(center_x,center_y),3,(255,0,255),-1)

    cv2.imshow('Mask', mask1)
    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
cv2.destroyAllWindows()