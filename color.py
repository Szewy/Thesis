import cv2 
import numpy as np  
import time

cap = cv2.VideoCapture('stone.mp4')  
  
i = 1;
f = open("frames.txt", "a")

while(1):        
 
    _, frame = cap.read()  
  
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([98,50,20]) 
    upper_red = np.array([130,255,255]) 
	
#   lower_red = np.array([110,50,50]) 
#   upper_red = np.array([130,255,255]) 
  
    mask = cv2.inRange(hsv, lower_red, upper_red) 
  
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 
  
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'): 
        f.write(str(i)+"\n")
		
		
    time.sleep(0.15)
	
    i = i+1
	
cv2.destroyAllWindows() 
  
cap.release() 
