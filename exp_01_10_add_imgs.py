import cv2

img = cv2.imread('messi5.jpg')
img1 = cv2.imread('opencv-logo.png')

# adding of two images
img = cv2.resize(img,(512,512)) # here the size of the images should be similar otherwise trace back will be coming
img1 = cv2.resize(img1,(512,512)) # so because of that we should resize before adding
out = cv2.add(img,img1) # adding of two images | in here the matrices are added parallely so in here we an see one image over wirtten on another image 
# weighted addition 
out1 = cv2.addWeighted(img,0.7,img1,0.3,0) # source1, weightage os 1St image, source2,  weightage os 1St image,scalar value | The overall weigtage should be 1 so write it likewise

cv2.imshow('weighted_image',out1)
cv2.imshow('Adde_image', out)
cv2.waitKey(0)

cv2.destroyAllWindows()