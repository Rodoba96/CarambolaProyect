
import cv2
from cv2 import VideoCapture
import numpy as np

#Ranges for yellow H   S   V(default)
lower_yellow = np.array([15, 80, 95])
upper_yellow = np.array([25, 255, 255])

#RED
#lower = np.array([0, 150, 20])
#upper = np.array([10, 255, 255])

#Imagenes
#Images
#img = cv2.imread('D:\Documentos\MisProyectos\CarambolaProyect\Carambola_Proy\imagenes\muestra_01.jpg')

#Video
cap = cv2.VideoCapture(0)


while True:

    ret,frame = cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convert the image into HSV
    #image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Convert the image into HSV
    
    mask1 = cv2.inRange(image, lower_yellow, upper_yellow)

    contours, hierarchy = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) !=0:
        for contour in contours:
            if cv2.contourArea(contour) > 360:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),3)
                #cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                center_x = x+(w//2)
                center_y = y+(h//2)
                cv2.circle(frame,(center_x,center_y),3,(255,255,255),-1)
                #cv2.circle(img,(center_x,center_y),3,(255,0,255),-1)

    cv2.imshow('Mask', mask1)
    cv2.imshow('webcam', frame)
    #cv2.imshow('webcam', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()