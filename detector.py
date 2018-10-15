import cv2
import numpy as np

from pathlib import Path

k = 1;


while Path("stone_getter/" + str(k) + ".bmp").is_file():
  img = cv2.imread("stone_getter/" + str(k) + ".bmp")
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

  retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY)

  image, contours, hierarchy = cv2.findContours(thresh_gray,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

  mx = (0,0,0,0)      
  mx_area = 0

  for cont in contours:
    x,y,w,h = cv2.boundingRect(cont)
    area = w*h
    
    if area > mx_area:
      mx = x,y,w,h
      mx_area = area
		
  x,y,w,h = mx

  roi=img[y:y+h,x:x+w]
  cv2.imwrite("stone_detector/"+str(k)+".bmp", roi)
  k=k+1