import cv2
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png')

_, th1 = cv2.threshold(img,127.5,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,127.5,255,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img,127.5,255,cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img,127.5,255,cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img,127.5,255,cv2.THRESH_TOZERO_INV)


titles = ['original_image','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV']
images = [img,th1,th2,th3,th4,th5] #give the image variables in the same order of titles

for i in range(6):
    plt.subplot(2,3,i+1) # row, column, incrimentation order
    plt.imshow(images[i],'gray') #gray denote the color
    plt.title(titles[i]) # this is to be given otherwise titles will not be printed
    plt.xticks([]), plt.yticks([])  #these are syntax for not printing x and y axis variables

plt.show()

#code for printing single image
#while reading the image the image would be in BGR format but matplot takes images as RGB format so conversion is to be done
# so the code given below is image after reading
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     plt.imshow(img)
#     plt.show() 

