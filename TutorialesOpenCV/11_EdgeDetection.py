import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagenes/lena256x256 Color.jpg')

# Threshold values between 0 and 255
edges = cv2.Canny(img,threshold1=127, threshold2=127)
# To chosse a better threshold values:
med_val = np.median(img)
    # 1. Lower threshold to either 0 or 70% of the median value wichever is greater
lower = int(max(0,0.7*med_val))
    # 2. Upper threshold to eithe 130% of the median or the max 255, wichever is smaller
upper = int(min(255,1.3*med_val))
    # Blurring can improve the edge detector:
blurred_img = cv2.blur(img,ksize=(5,5))


edges2 = cv2.Canny(img,threshold1=lower, threshold2=upper)
edges3 = cv2.Canny(blurred_img,threshold1=lower, threshold2=upper)

while True:
    #cv2.imshow('OG', img)
    cv2.imshow('Test', edges)
    cv2.imshow('Test 2', edges2)
    cv2.imshow('Test 3', edges3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

