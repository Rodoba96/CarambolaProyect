import cv2

# Read an image
img = cv2.imread('imagenes/color_image.jpeg')

while True:
    #Show image
    cv2.imshow('Image' , img)

    #If we've waited at least 1 ms AND we've presed the ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

