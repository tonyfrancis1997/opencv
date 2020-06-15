import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') #XVID is the fourcc code  
out = cv2.VideoWriter('output.avi',fourcc,20,(640,480))


while(True):
    ret, frame = cap.read() #ret is the boolean function of the frame
    if ret ==True: #ret will be true when frame is there otherwise it would be false
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#these are for finding the prop of the frame 
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #for colour conversion
        cv2.imshow('frame',gray) #for displaying the video
    
        if cv2.waitKey(1) & 0xFF == ord('q'): #this like a delay to say how much time the video window should be open
            break

 #at the end of every program we should release the instances and destroy all the open windows   
cap.release()
out.release()
cv2.destroyAllWindows()