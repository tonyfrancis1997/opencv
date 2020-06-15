import cv2
img =  cv2.imread('lena.jpg',1)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyWindow('image')

cv2.imwrite('lena_gray.jpg',img) #writing image


