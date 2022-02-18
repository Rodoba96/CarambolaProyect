import cv2

cap = cv2.VideoCapture(0)

# Capture the width and height of the frame to save later
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = width // 2 # // --> Regresa un entero
y = height // 2

# Width and height of Rectangle
w = width // 4 # // --> Regresa un entero
h = height // 4

# BOTTOM RIGHT x + w, y+h

while True:

    ret,frame = cap.read()

    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=4)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
