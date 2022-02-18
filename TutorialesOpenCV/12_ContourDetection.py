import cv2
from cv2 import findContours
import numpy as np

img = cv2.imread('imagenes/lena256x256 Color.jpg',0)
contours,hierarchy = cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

external_contours = np.zeros(img.shape)

for i in range(len(contours)):
    #External
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(external_contours,contours, i, 255, -1)



while True:
    cv2.imshow('Test', img)
    cv2.imshow('Test 2', external_contours)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()