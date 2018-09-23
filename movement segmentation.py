import numpy as np
import cv2
import time

cap = cv2.VideoCapture('test.mp4')
#cap = cv2.VideoCapture(0)

#fgbg = cv2.createBackgroundSubtractorMOG2(0, 10, False)
#fgbg = cv2.createBackgroundSubtractorMOG2(300, 32, False)

fgbg = cv2.createBackgroundSubtractorKNN(200, 8, False)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))

while True:
    ret, frame = cap.read()
	
    #frame = cv2.blur(frame,(5,5))
	
    frame = cv2.flip(frame, flipCode=1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
    frame = cv2.bilateralFilter(frame,9,75,75)
 
    fgmask = fgbg.apply(frame)
    
    #fgmask = cv2.erode(fgmask,kernel,iterations = 1)
    #fgmask = cv2.dilate(fgmask,kernel,iterations = 1)
	
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    
    #fgmask = cv2.filter2D(fgmask,-1,kernel)
    #fgmask = cv2.dilate(fgmask,kernel,iterations = 1)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel2)
    
	#fgmask = cv2.medianBlur(fgmask, 5)
    #fgmask = cv2.GaussianBlur(fgmask, (5,5), 0)
	
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_GRADIENT, kernel2)
	
    #fgmask = cv2.Canny(fgmask,100,200)
	
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
		
    time.sleep(0.09)
	
cap.release()
cv2.destroyAllWindows()