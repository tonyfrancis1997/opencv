import cv2
import numpy as np 
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png',0)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
# DIALATION OPERATION
kernel = np.ones((2,2),np.uint8) # creating a rectangular kernel| give kernel bock small as possible or else more area will be dialated than the original image | and also increase in iteration will aslo result in extra dialation
dialat = cv2.dilate(mask,kernel,iterations=2)
eroded = cv2.erode(mask,kernel,iterations=1)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #erosion followed by dialation
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel) # dialation followed by erosion
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #difference between dialatio and erosion
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel) #diff b/w img & opening of the image



titles = ['org_image','mask','dialated','eroded','opening','closing','mg','th']
images = [img,mask,dialat,eroded,opening,closing,mg,th] #give the image variables in the same order of titles

for i in range(8):
    plt.subplot(2,4,i+1) # row, column, incrimentation order
    plt.imshow(images[i],'gray') #gray denote the color
    plt.title(titles[i]) # this is to be given otherwise titles will not be printed
    plt.xticks([]), plt.yticks([])  #these are syntax for not printing x and y axis variables

plt.show()