import cv2
img = cv2.imread('gradient.png')

_, th1 = cv2.threshold(img,127.5,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,127.5,255,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img,127.5,255,cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img,127.5,255,cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img,127.5,255,cv2.THRESH_TOZERO_INV)
_, th6 = cv2.threshold(img,127.5,255,cv2.THRESH_MASK)
#_, th3 = cv2.threshold(img,127.5,255,cv2.THRESH_TRUNC)

cv2.imshow('image',img)
cv2.imshow('threshold_bin',th1)
cv2.imshow('threshold_bin_inv',th2)
cv2.imshow('threshold_trunc',th3)
cv2.imshow('threshold_tozero',th4)
cv2.imshow('threshold_tozero_inv',th5)
cv2.imshow('threshold_mask',th6)
#cv2.imshow('thhreshold_tozero',th4)

cv2.waitKey(0)
cv2.destroyAllWindows()