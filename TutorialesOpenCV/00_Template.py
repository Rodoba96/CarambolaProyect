import cv2
#import numpy as np
#import matplotlib.pyplot as plt

#Images
lena = cv2.imread('imagenes/lena256x256 Color.jpg', 0)

#Video
cap = cv2.VideoCapture(0)


while True:
    cv2.imshow('Test Image', lena)

    ret,frame = cap.read()
    cv2.imshow('Test', frame)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()