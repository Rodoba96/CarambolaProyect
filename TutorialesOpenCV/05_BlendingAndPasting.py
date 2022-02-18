import cv2
import numpy as np
import matplotlib.pyplot as plt


img1 = cv2.imread('imagenes/lena256x256 Color.jpg') #Small image
#img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2 = cv2.imread('imagenes/color_image.jpeg') #Big image
#img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

# Resize images to the sae size
img1_resized = cv2.resize(img1,(256,256)) 
img2_resized = cv2.resize(img2,(256,256))

blended = cv2.addWeighted(src1=img1_resized, alpha=0.5, src2=img2_resized, beta=0.5, gamma=0)

# Overlay small image on top of a larger image (No blending)
# Numpy reassignment

#Blend Together images of different sizes

large_img = img2
small_img = img1

x_offset = 0 
y_offset = 0

x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]

large_img[y_offset:y_end,x_offset:x_end] = small_img

while True:
    #cv2.imshow('my_Image', img1)
    #cv2.imshow('my_Image2', img2)
    cv2.imshow('Blended Image', blended)
    cv2.imshow('Overlay Image', large_img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
