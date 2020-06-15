import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

lap = cv2.Laplacian(img,cv2.CV_64F,ksize=1) # laplacian methon of edge detection|kernel size must be an odd number
lap = np.uint8(np.absolute(lap)) # to find absolute 
sobelx= cv2.Sobel(img,cv2.CV_64F,1,0) # sobel_x method | the last two variable determine sobel x or y |helps to find directional change in vertical direction
sobely= cv2.Sobel(img,cv2.CV_64F,0,1) # sobel_y method | helps to find directional change in horizontal direction
canedge = cv2.Canny(img,100,200) #this is used to get more precise edges in images
# converting these above variable into unsigned int
sobelx = np.uint8(np.absolute(sobelx)) # to find absolute 
sobely = np.uint8(np.absolute(sobely)) # to find absolute 

sobel_comb = cv2.bitwise_or(sobelx,sobely)

titles = ['orginal','laplacian','sobelx','sobely','sobel_comb','canedge']
images = [img, lap,sobelx,sobely,sobel_comb,canedge]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()