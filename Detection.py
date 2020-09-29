import numpy as np
import pandas as pd
import cv2 as cv

img = cv.imread('test.jpg')
image = cv.imread('test.jpg')
frm = cv.imread('test.jpg')


img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_red = np.array([0   ,  60  ,  150])
upper_red = np.array([180 , 255  ,  255])

mask = cv.inRange(img, lower_red, upper_red)

kernal = np.ones((5,5), np.uint8)
erode = cv.erode(mask, kernal)

contours, _ = cv.findContours(erode, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    
    x,y,w,h = cv.boundingRect(cnt)

    area = cv.contourArea(cnt)
    if area > 100 and area < 10000:
        cv.rectangle(frm, (x,y),(x+w,y+h), (0,255,0), 2)
    

for c in contours:
    
    x,y,w,h = cv.boundingRect(cnt)
    area = cv.contourArea(cnt)
    
    if area > 100:

        acc = 0.01 * cv.arcLength(c,True)
        approx = cv.approxPolyDP(c, acc , True)
        cv.drawContours(image, [approx], -1 ,(0,0,255), 2)       
    
    
cv.imwrite('h.jpg',frm)
cv.imwrite('e.jpg',erode)
cv.imwrite('m.jpg',mask)
cv.imwrite('orig.jpg', image)