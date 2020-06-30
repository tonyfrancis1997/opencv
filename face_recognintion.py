import cv2
import numpy as np
import pickle

labels = {}

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Creating recognizer to recognize images
recognizer =  cv2.face.LBPHFaceRecognizer_create(radius=15,neighbors=10,grid_x=20,grid_y=25)
recognizer.read("trainner.yml") # Reading the trained data
# LOading the image labels from files
with open("label.pickle","rb") as file: # this pickle is used for storing the data in bytes into a file |rb denote reading byte
    labels_blah = pickle.load(file)
    labels = {v:k for k,v in labels_blah.items()} # reversing the order of keys and values

while(cap.isOpened()):
    _, frame = cap.read()
    #converting to gray scale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    roi = frame.copy()
    #determing the edges
    faces = face_cascade.detectMultiScale(gray,1.1,25)
    for (x, y, w, h) in faces:
        roi = roi[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]# creating the region of interest i.e the face image
        # predicting the image
        id_,conf = recognizer.predict(roi_gray) # it gives two things id and confidence
        print(id_)
        if conf> 60 and conf<=175:
            cv2.putText(frame,labels[id_],(w+x,h+y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,2,240),2)
        #    print(id_)
        #    print(labels[id_])
        cv2.imwrite('tony.jpg',roi)
        cv2.rectangle(frame,(x,y),(w+x,h+y),(0,255,0),2)# Drawing the rectangle
        
        
    cv2.imshow('face_detection',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()