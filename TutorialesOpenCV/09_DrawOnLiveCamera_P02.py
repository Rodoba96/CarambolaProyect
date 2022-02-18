import cv2


## CALLBACK FUNCTION RECTANGLE
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_isClicked, botRight_isClicked

    if event == cv2.EVENT_LBUTTONDOWN:
        
        #Reset the rectangle
        if topLeft_isClicked == True and botRight_isClicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_isClicked = False
            botRight_isClicked = False

        if topLeft_isClicked == False:
            pt1 = (x,y)
            topLeft_isClicked = True
        
        elif botRight_isClicked == False:
            pt2 = (x,y)
            botRight_isClicked = True


## GLOBAL VARIABLES
pt1 = (0,0)
pt2 = (0,0)
topLeft_isClicked = False
botRight_isClicked = False

## CONNECT TO TE CALLBACK
cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)

while True:

    ret,frame = cap.read()

    ## DRAWING ON THE FRAME BASED OFF THE GLOBAL VARIABLES
    if topLeft_isClicked == True:
        cv2.circle(frame,center=pt1, radius=2, color=(0,0,255),thickness=-1)
    
    if topLeft_isClicked == True and botRight_isClicked == True:
        cv2.rectangle(frame,pt1 ,pt2, (0,0,255), 3)
    
    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
