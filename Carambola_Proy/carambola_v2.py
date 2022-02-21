#Referencias:
#
# https://www.youtube.com/watch?v=cMJwqxskyek
# https://www.youtube.com/watch?v=nty0zSKB4_k

import cv2
from cv2 import VideoCapture
import numpy as np
import math

def calculateDistance(x1,y1,x2,y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def calculateAngles(a,b,c):
    #Trigonometric properties
    ang_A = math.acos(((b**2)+(c**2)-(a**2))/(2*b*c))
    ang_B = math.acos(((a**2)+(c**2)-(b**2))/(2*a*c))
    ang_C = math.acos(((a**2)+(b**2)-(c**2))/(2*a*b))
    #Rad to Deg
    ang_A = ang_A * 180/math.pi
    ang_B = ang_B * 180/math.pi
    ang_C = ang_C * 180/math.pi
    return ang_A, ang_B, ang_C

#Ranges for yellow H   S   V(default)
lower_yellow = np.array([20, 130, 20])
upper_yellow = np.array([30, 255, 255])

#RED
lower_red = np.array([170, 150, 20])
upper_red = np.array([180, 255, 255])

#White 
lower_white = np.array([0, 0, 100])
upper_white = np.array([80, 150, 255])

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
            if cv2.contourArea(i) < 638 and cv2.contourArea(i) > 360:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,255),3)
                #cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                centerY_x = x+(w//2)
                centerY_y = y+(h//2)
                cv2.circle(frame,(centerY_x,centerY_y),3,(255,0,255),-1)
                #cv2.circle(img,(center_x,center_y),3,(255,0,255),-1)
        #Red contours
        for i in contours2:
            if cv2.contourArea(i) > 500:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),3)
                #cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                centerR_x = x+(w//2)
                centerR_y = y+(h//2)
                cv2.circle(frame,(centerR_x,centerR_y),3,(255,0,255),-1)
                #cv2.circle(img,(center_x,center_y),3,(255,0,255),-1)
        #White contours
        for i in contours3:
            if cv2.contourArea(i) < 925 and cv2.contourArea(i) > 380: 
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(frame,(x,y),(x+w, y+h),(255,255,255),3)
                #cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                centerW_x = x+(w//2)
                centerW_y = y+(h//2)
                cv2.circle(frame,(centerW_x,centerW_y),3,(255,0,255),-1)
                #cv2.circle(img,(center_x,center_y),3,(255,0,255),-1)
        
        #Draw a trianlge
        cv2.line(img=frame, pt1=(centerY_x,centerY_y),pt2=(centerR_x,centerR_y),color=(255,0,255),thickness=2) # Yellow - Red
        cv2.line(img=frame, pt1=(centerR_x,centerR_y),pt2=(centerW_x,centerW_y),color=(255,0,255),thickness=2) # Red    - White
        cv2.line(img=frame, pt1=(centerW_x,centerW_y),pt2=(centerY_x,centerY_y),color=(255,0,255),thickness=2) # White  - Yellow

        #Obtain distance 
        dist_YR = calculateDistance(centerY_x,centerY_y,centerR_x,centerR_y)
        dist_RW = calculateDistance(centerR_x,centerR_y,centerW_x,centerW_y)
        dist_WY = calculateDistance(centerW_x,centerW_y,centerY_x,centerY_y) 

        #Obtain Angles
        ang_YWR, ang_RYW, ang_WRY = calculateAngles(dist_YR,dist_RW,dist_WY)
        

    #cv2.imshow('Mask', mask3)
    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#cap.release()
cv2.destroyAllWindows()


print(dist_YR)
print(dist_RW)
print(dist_WY)
print()
print(ang_YWR)
print(ang_RYW)
print(ang_WRY)

print(ang_YWR+ang_RYW+ang_WRY)