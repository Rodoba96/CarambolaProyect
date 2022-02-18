import cv2


## CALLBACK FUNCTION Circle
def draw_circle(event, x, y, flags, param):
    global pt1, isClicked

    if event == cv2.EVENT_LBUTTONDOWN:
        
        #Reset the circle
        if isClicked == True:
            pt1 = (0,0)
            isClicked = False

        if isClicked == False:
            pt1 = (x,y)
            isClicked = True


## GLOBAL VARIABLES
pt1 = (0,0)
isClicked = False

## CONNECT TO TE CALLBACK
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_circle)

while True:

    ret,frame = cap.read()

    ## DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    if isClicked == True:
        cv2.circle(frame,center=pt1, radius=50, color=(0,0,255),thickness=2)
    
    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
