import cv2
import numpy as np

def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        B = img[y ,x, 0]
        G = img[y, x, 1]
        R = img[y, x, 2]
        clrimg = np.zeros((512,512,3),np.uint8) #this is for making a window with balck color| the first argument is the dimension and number of channel inputs and the next argument is the data type
        clrimg[:] = [B,G,R] #clrimg[:] statement specify to fill each pixel with the incoming data that is the BGR value
        cv2.imshow('COLOR',clrimg)

points = []
img = cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)

cv2.destroyAllWindows()


