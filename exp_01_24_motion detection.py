import cv2
import numpy as np 

cap = cv2.VideoCapture('vtest.avi')

# 1.Reading the frame
ret , frame1 = cap.read()
ret , frame2 = cap.read()

while cap.isOpened():
    #2.finding absolute difference
    diff = cv2.absdiff(frame1,frame2)
    #3.gray scale conversion
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    #4.finding blur image
    blur = cv2.GaussianBlur(gray,(5,5),0)
    #5.finding threshold of blured image
    _, th = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    #6. dialation
    dialated = cv2.dilate(th,None,iterations=3)
    #7.finding contours
    contours,_ = cv2.findContours(dialated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #8.Drawing contours
    #cv2.drawContours(frame1,contour,-1,(0,255,0),2)
      # Drawing rectangle
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) <900: #this is avoid small object movemnents
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2) #drwaing rectangles with coordinates obtained from bounding rectangle in line 27


    cv2.imshow("video",frame1)

    #reading new frames
    frame1 = frame2
    _,frame2 = cap.read()
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
