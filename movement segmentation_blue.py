import numpy as np
import cv2
import time

cap = cv2.VideoCapture('stone.mp4')
#cap = cv2.VideoCapture(0)

#fgbg = cv2.createBackgroundSubtractorMOG2(0, 10, False)
#fgbg = cv2.createBackgroundSubtractorMOG2(300, 32, False)

fgbg = cv2.createBackgroundSubtractorKNN(300, 8, False)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))

i = 1;
f = open("frames.txt", "a")

while True:
    ret, frame = cap.read()
	
    #frame = cv2.GaussianBlur(frame, (5,5), 0)
	
    frame = cv2.flip(frame, flipCode=1)
		
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([98,50,20]) 
    upper_red = np.array([130,255,255]) 
    mask = cv2.inRange(hsv, lower_red, upper_red)
	
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
    fgmask = fgbg.apply(frame)
    
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    
    #fgmask = cv2.filter2D(fgmask,-1,kernel)
    #fgmask = cv2.dilate(fgmask,kernel,iterations = 1)
    
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel2)
	
    res = cv2.bitwise_and(fgmask,mask)
    
    cv2.imshow('frame', res)
	
    k = cv2.waitKey(1) & 0xFF
    if k == ord('a'): 
        f.write(str(i)+"\n")
		
    if k == ord('q'):
        break
		
    time.sleep(0.12)
	
    i = i+1
	
cap.release()
cv2.destroyAllWindows()