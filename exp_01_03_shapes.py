import cv2
img =  cv2.imread('lena.jpg',1)

img = cv2.line(img,(0,0),(255,255),(255,140,90),3) #drawing line to the image
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),3)#drawing arrowed line
img = cv2.rectangle(img,(255,0),(410,300),(255,150,10),2)# drawing rectangle
img = cv2.circle(img,(440,300),60,(30,230,180),-1) #drawing circle ((-1 will give the whole circle colour ))
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX #defining the font type
img =  cv2.putText(img,'THIS is LenA',(0,300),font,2,(250,230,45),3,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyWindow('image')

cv2.imwrite('lena_gray.jpg',img) #writing image


