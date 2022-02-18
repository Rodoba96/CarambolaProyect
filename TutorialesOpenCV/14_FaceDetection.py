import cv2
import numpy as np
import matplotlib.pyplot as plt

lena = cv2.imread('imagenes/lena256x256 Color.jpg', 0)
lenna_mature = cv2.imread('imagenes/lenna_mature.jpg', 0)

#Se necesita un clasificador cascaa entrenado

while True:
    cv2.imshow('Test Image', lena)
    cv2.imshow('Test Image 2', lenna_mature)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

