import cv2
import numpy as np


#################
### FUNCTIONS ###
#################

def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img,center=(x,y),radius=50,color=(0,255,0),thickness=-1)
        #                        B  G  R
        cv2.circle(img,(x,y),50,(0,255,0),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,0,0),-1)

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_circle)

#################################
### SHOWING IMAGE WITH OPENCV ###
#################################

img = np.zeros((512,512,3),np.uint8)

while True:
    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
