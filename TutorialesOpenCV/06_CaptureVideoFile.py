from turtle import width
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0) # 0 is the default camera

# Capture the width and height of the frame to save later
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Save the video file
writer = cv2.VideoWriter('imagenes/mysupervideo.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))

while True:
    
    ret,frame = cap.read()

    # OPERATIONS (Drawings)
    writer.write(frame)

    cv2.imshow('Frame', frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame Gray', gray)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()