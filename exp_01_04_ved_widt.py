import cv2
import datetime
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#these are for finding the prop of the frame 
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


cap.set(cv2.CAP_PROP_FRAME_HEIGHT,700)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#these are for finding the prop of the frame 
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        txt = 'width :'+str(cap.get(3))+'  Height :'+str(cap.get(4)) #here 3 and 4 dente the property numbers they denote width and height prop respectively
        datet  = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet,(10,40),font,2,(200,230,180),3,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #this like a delay to say how much time the video window should be open
            break
cap.release()

cv2.destroyAllWindows()


