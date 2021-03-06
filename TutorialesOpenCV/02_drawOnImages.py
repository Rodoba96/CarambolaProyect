import cv2
import numpy as np
import matplotlib.pyplot as plt

#Create a blank image
blank_img = np.zeros(shape=(512,512,3),dtype=np.uint8)

#Draw figures
cv2.rectangle(blank_img, pt1=(384,10),pt2=(500,150),color=(0,255,0),thickness=10)
    #Circles
cv2.circle(img=blank_img, center=(200,200),radius=50,color=(255,0,0),thickness=8)
    #filled circle
cv2.circle(img=blank_img, center=(100,100),radius=50,color=(255,0,0),thickness=-1)
    #Lines
cv2.line(img=blank_img, pt1=(0,0), pt2=(512,512), color=(102,255,255), thickness=5)

#Text
font = cv2.FONT_HERSHEY_SIMPLEX #Select the font
cv2.putText(img=blank_img, text='Hello',org=(10,500),fontFace=font, fontScale=4, color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)

#Poligons
#vertices = np.array([ [100,300], [200,200], [400,300], [200,400] ], dtype=np.int32)
#pts = vertices.reshape((-1,1,2))
#cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0), thickness=5)


while True:
    #Show blanck image
    cv2.imshow('Blank Image' , blank_img)
    #If we've waited at least 1 ms AND we've presed the ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
