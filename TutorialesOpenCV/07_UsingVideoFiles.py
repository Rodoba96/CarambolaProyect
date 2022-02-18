import cv2
import time

cap = cv2.VideoCapture('imagenes/myspuervideo.mp4')

if cap.isOpened() == False:
    print('ERROR FILE NOT FOUND OR WRONG CODEC USED!')

while cap.isOpened():

    ret,frame = cap.read()

    if ret == True:
        
        # Writer 20 FPS
        time.sleep(1/20)
        cv2.imshow('Frame', frame)
        
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()