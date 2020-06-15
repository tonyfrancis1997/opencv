import cv2

img = cv2.imread('sudoku.png',0)

th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
#th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
#th4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 12)
#th5 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 14)
#th6 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 16)
#th7 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 18)



cv2.imshow('org_image',img)
cv2.imshow('thresh_mean_c1',th1)
cv2.imshow('thresh_mean_c2',th2)
#cv2.imshow('thresh_mean_c3',th3)
#cv2.imshow('thresh_mean_c4',th4)
#cv2.imshow('thresh_mean_c5',th5)
#cv2.imshow('thresh_mean_c6',th6)
#cv2.imshow('thresh_mean_c7',th7)


cv2.waitKey(0)

cv2.destroyAllWindows()
