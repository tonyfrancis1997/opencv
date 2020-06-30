import os
import cv2
import numpy as np
from PIL import Image # PIL is the image library of python
import pickle
print("training..")
x_train = []
y_labels = []
label_ids = {} # creating a dictionary for labels
current_id = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#finding the path where this python file is saved
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# FInding the Image directory
image_dir = os.path.join(BASE_DIR, "images")
print("..")
# Walking through images directory to find images
for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jfif"):
            path = os.path.join(root,file) #this will give out the path of each image
            label = os.path.basename(os.path.dirname(path)) # finding the name of each folder in image directory
            print("..")
            #print(label,path)
            if not label  in label_ids:
                label_ids[label] = current_id
                current_id += 1
                print("..")
            id_ = label_ids[label] # labels and ids associated with each label is stored in id_

            pil_image = Image.open(path).convert("L") #it converts the image into grayscale
            #creating a numpy array
            image_array = np.array(pil_image,"uint8")# we are going to train the image on this numpy array
            # Finding region of interest
            faces = face_cascade.detectMultiScale(image_array, 1.1, 55)
            for (x,y,w,h) in faces:
                print("..")
                roi = image_array[y:y+h , x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
print("..")
with open("label.pickle","wb") as file: # this pickle is used for storing the data in bytes into a file |wb denote writing byte
    pickle.dump(label_ids,file)

# intialising recogniser
recognizer =  cv2.face.LBPHFaceRecognizer_create()
recognizer.train(x_train,np.array(y_labels))
recognizer.save("trainner.yml")
print('trained')



