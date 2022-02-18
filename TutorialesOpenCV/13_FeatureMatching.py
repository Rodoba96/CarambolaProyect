import cv2
import numpy as np
import matplotlib.pyplot as plt
###################################

def display(img,cmap='gray'):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

img1 = cv2.imread('imagenes/lena256x256 Color.jpg',0)
img2 = cv2.imread('imagenes/lena256x256 Color.jpg',0)

# Create detection object
orb = cv2.ORB_create()
#kp1,des1 = orb.detectAndCompute(img1,None)
#kp2,des2 = orb.detectAndCompute(img2,None)

# Create the matching objects
#bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
#matches = bf.match(des1,des2)

#matches = sorted(matches, key=lambda x:x.distance)
#img_matches = cv2.drawMatches(img1,kp1,img2,kp2,matches[:25],None,flags=2)

## PART 2

# Create a Sif object
sift = cv2.xfeatures2d.SIFT_create()
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
good = []

for match1,match2 in matches:
    # If match 1 distance is less than 75% of match 2 distance
    # then descriptor was good match, lets keep it!
    if match1.distance < 0.75*match2.distance:
        good.append([match1])

sift_matches = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

while True:
    #cv2.imshow('Test', img1)
    #cv2.imshow('Test 2', img2)
    #cv2.imshow('Test 3', img_matches)
    cv2.imshow('Test 4', sift_matches)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()