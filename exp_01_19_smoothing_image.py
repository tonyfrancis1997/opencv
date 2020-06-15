import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('lena.jpg',1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5),np.float32)/25 # creating kernel by dividing 5x5 array of ones with 25(i.e height * width)
dst = cv2.filter2D(img,-1,kernel) #2D convolution using hmogeneous filter
blur = cv2.blur(img,(5,5)) #blur method
gblur = cv2.GaussianBlur(img,(5,5),0) # image variable|kernel|sigma value
median = cv2.medianBlur(img,5) # give kernel value as odd number which is grater than zero|it replace each pixel value with neighbouring pixel value
bil_fliter = cv2.bilateralFilter(img,3,75,75)# bilateral filter used to sharpen images| it keeps edges sharp in images

titles = ['orginal','smoothened','blur','gblur','median','bil_fliter']
images = [img, dst,blur,gblur,median,bil_fliter]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()