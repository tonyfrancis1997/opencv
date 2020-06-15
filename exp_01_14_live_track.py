import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cv2.namedWindow('tracking')


def track(x):
    pass

# Creating trackbar for the image | This trackbar is for the hsv values
cv2.createTrackbar('l_h','tracking',0,255,track)
cv2.createTrackbar('l_s','tracking',0,255,track)
cv2.createTrackbar('l_v','tracking',0,255,track)

cv2.createTrackbar('u_h','tracking',255,255,track)
cv2.createTrackbar('u_s','tracking',255,255,track)
cv2.createTrackbar('u_v','tracking',255,255,track)


while(1):
    _,img = cap.read() #this read operation gives two values one is boolean and other one is the image itself | in here i don't ned boolean value so that is why i ahd given it as '_,'

    #hsv converstion
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #obtaining trackbar posions of the image
    l_h1 = cv2.getTrackbarPos('l_h','tracking')
    l_s1 = cv2.getTrackbarPos('l_s','tracking')
    l_v1 = cv2.getTrackbarPos('l_v','tracking')

    u_h1 = cv2.getTrackbarPos('u_h','tracking')
    u_s1 = cv2.getTrackbarPos('u_s','tracking')
    u_v1 = cv2.getTrackbarPos('u_v','tracking')

    # lower bind and upper bind values
    l_b = np.array([l_h1,l_s1,l_v1])
    u_b = np.array([u_h1,u_s1,u_v1])

    #masking | In here mask is created in range of upper and lower bind hsv values
    mask = cv2.inRange(hsv,l_b,u_b)

    res = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('org_img',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

