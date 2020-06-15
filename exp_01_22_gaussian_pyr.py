import cv2

img  = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]
# PYRDOWN --reducing the resolution
lr1 = cv2.pyrDown(img) 
lr2 = cv2.pyrDown(lr1) 

# PYRUP --increasing resolution
up1 = cv2.pyrUp(img)       

#PYRup or down using for loop
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

#laplacian pyramid 
lena_copy = gp[5]
lp_lena = [lena_copy]
for i in range(5,0,-1):
    gaus_ext = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract((gp[i-1]),gaus_ext)
    lp_lena.append(laplacian)
    cv2.imshow(str(i), laplacian) 

cv2.imshow('org',img)
cv2.imshow('lower_resolution1',lr1)
cv2.imshow('lower_resolution2',lr2)
cv2.imshow('incr_resolution1',up1)
cv2.waitKey(0)

cv2.destroyAllWindows()