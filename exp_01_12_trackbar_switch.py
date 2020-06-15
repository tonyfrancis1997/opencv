import cv2
import numpy as np 

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

def track(x):
    print(x)

# Creating trackbar for the image
cv2.createTrackbar('B','image',0,255,track)
cv2.createTrackbar('G','image',0,255,track)
cv2.createTrackbar('R','image',0,255,track)




while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    #obtaining trackbar posions of the image
    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')

    img[:] = [b,g,r] #changing image w,r,t track bar input 

cv2.destroyAllWindows()