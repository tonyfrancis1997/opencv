import cv2
import numpy as np 

img = cv2.imread('bAw.png')
img = cv2.resize(img,(300,200))
img1 = np.zeros((200,300,3),np.uint8)
img1 = cv2.rectangle(img1,(100,0),(250,50),(255,255,255),-1)

#ANd operation
bit_And = cv2.bitwise_and(img1,img)
#OR operation
bit_OR = cv2.bitwise_or(img1,img)
#NOT operation
bit_NOT = cv2.bitwise_not(img)
bit_NOT1 = cv2.bitwise_not(img1)
#XOR operation
bit_XOR = cv2.bitwise_xor(img,img1)

cv2.imshow('AND',bit_And)#and operation output
cv2.imshow('OR',bit_OR)# OR operation output
cv2.imshow('NOT',bit_NOT)# not operation output1
cv2.imshow('NOT1',bit_NOT1)# not operation output2
cv2.imshow('XOR',bit_XOR)#xor opertion output
cv2.imshow('white_rect_in_black',img1)
cv2.imshow('black_white',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
