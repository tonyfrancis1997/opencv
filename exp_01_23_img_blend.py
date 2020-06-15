import cv2
import numpy as np 

orange = cv2.imread('orange.jpg')
apple = cv2.imread('apple.jpg')

# simple merging of two images without blending
a_o = np.hstack((apple[:, :256],orange[:,256:]))

# IMAGE BLENDING using IMAGE PYRAMID technique has 5 steps
# 1.Load the 2 images 
# 2. Find gausian pyramids for both the images
# 3. From gausian pyramids fing their laplacian pyramids
# 4.Now join left and right half of both the images in different layers of laplacian pyramids
# 5.Finally from this joint image pyramids, reconstruct original image

# step 2:
# Gausian pyramid of orange
orange_copy = orange.copy()
gp_o = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_o.append(orange_copy)
# Gausian pyramid of apple
apple_copy = apple.copy()
gp_a = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_a.append(apple_copy)

# step 3:
# Laplacian pyramid of orange
orange_copy = gp_o[5]
lap_o = [orange_copy]
for i in range(5,0,-1):
    gaus_ext = cv2.pyrUp(gp_o[i])
    laplac = cv2.subtract(gp_o[i-1],gaus_ext)
    lap_o.append(laplac)
# Laplacian pyramid of apple
apple_copy = gp_a[5]
lap_a = [apple_copy]
for i in range(5,0,-1):
    gaus_ext = cv2.pyrUp(gp_a[i])
    laplac = cv2.subtract(gp_a[i-1],gaus_ext)
    lap_a.append(laplac)

# step 4:
# joining of two images
apple_orange_pyr = []

for apple_l, orange_l in zip(lap_a,lap_o):
    col,row,ch = apple_l.shape
    laplacian = np.hstack((apple_l[:, :int(col/2)], orange_l[:,int(col/2): ]))
    apple_orange_pyr.append(laplacian)

# step 5:
# Reconstructing two images
# in this the image in 0TH position of 'apple_orange_pyr' will pyrupped and get added to the 1st pos of 'apple_orange_pyr' image
apple_orange_reconstruct = apple_orange_pyr[0]
for i in range(1,6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyr[i],apple_orange_reconstruct)

                                                                          

cv2.imshow('orange',orange)
cv2.imshow('apple',apple)
cv2.imshow('combined',a_o)
cv2.imshow('blended image',apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()