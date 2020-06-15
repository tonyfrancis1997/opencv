import cv2

img = cv2.imread('messi5.jpg')


# the below code is to copy and paste a portion of the image to the same image
ball = img[280:340 , 330:390] #these dimensions of of both should be same otherwise it will not paste in the in pos we require to paste
img[273:333 , 100:160] = ball


cv2.imshow('messi', img)
cv2.waitKey(0)

cv2.destroyAllWindows()

