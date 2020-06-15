import cv2

# this is for getting events list in cv2 directory
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strx = str(x) + ', '+ str(y)
        cv2.putText(img, strx, (x,y), font, 0.5, (255,255,0), 1)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y ,x, 0] #x and y are coordinates and '0' is the channel number for blue
        g = img[y, x, 1]
        r = img[y ,x, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        colr = str(b) + ', '+ str(g) + ', '+ str(r)
        cv2.putText(img, colr, (x,y), font, 0.5, (0,5,0), 1)
        cv2.imshow('image',img)

img = cv2.imread('messi5.jpg',1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event) #window name,fn name

cv2.waitKey(0)
  
cv2.destroyAllWindows()