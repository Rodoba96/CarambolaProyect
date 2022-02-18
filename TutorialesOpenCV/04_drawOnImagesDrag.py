import cv2
import numpy as np


### VARIABLES ###

# TRUE while mouse button DOWN, FALSE while mouse button UP
isDrawing = False
ix = -1
iy = -1

### FUNCTIONS ###

def draw_rectangle(event,x,y,flags,param):
    global ix, iy, isDrawing

    if event == cv2.EVENT_LBUTTONDOWN:
        isDrawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDrawing == True:
            cv2.rectangle(img, (ix,iy),(x,y),(0,255,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        isDrawing = False
        cv2.rectangle(img, (ix,iy),(x,y),(0,255,0),-1)



cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_rectangle)

#################################
### SHOWING IMAGE WITH OPENCV ###
#################################

#img = np.zeros((512,512,3),np.uint8)
img = np.zeros((512,512,3))

while True:
    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
