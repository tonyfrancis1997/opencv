import cv2

def click_event(event,x,y,flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),4,(0,230,180),-1)
        points.append((x,y))

        if len(points) >=2:
            cv2.line(img,points[-1],points[-2],(110,200,190),2)#here points[-1] depicts the last point and points[-2] depict the second last point
        cv2.imshow('image', img)

points = []
img = cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)

cv2.destroyAllWindows()


