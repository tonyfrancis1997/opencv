import cv2

img = cv2.imread('lena.jpg')

print(img.shape) # for finding the dimensions and chanel of the image
print(img.size) # it returns the no: of pixels in an image
print(img.dtype) # it returns the datatype of the image

b,g,r = cv2.split(img) # for splitting the image into 3 different channels i.e blue, green and red
img = cv2.merge((b,g,r)) # for merging the 3 channels if channels are only given

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
