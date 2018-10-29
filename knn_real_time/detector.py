import cv2
import numpy as np

from pathlib import Path

import x_y_size
import black_white_pixels

k = 1

def crop_minAreaRect(img, rect):
  angle = rect[2]
  rows,cols = img.shape[0], img.shape[1]
  matrix = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
  img_rot = cv2.warpAffine(img,matrix,(cols,rows))

  rect0 = (rect[0], rect[1], 0.0)
  box = cv2.boxPoints(rect)
  pts = np.int0(cv2.transform(np.array([box]), matrix))[0]
  pts[pts < 0] = 0

  return img_rot[pts[1][1]:pts[0][1], pts[1][0]:pts[2][0]]

def do(img):
  #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
  cv2.imwrite('gestures/' + str(0) + '.bmp', img)

  #retval, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY)

  image, contours, hierarchy = cv2.findContours(img,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

  mx_rect = (0,0,0,0)      
  mx_area = 0

  for cont in contours:
    arect = cv2.minAreaRect(cont)
    area = arect[1][0]*arect[1][1]
    if area > mx_area:
      mx_rect, mx_area = arect, area
	
  if mx_rect == (0, 0, 0, 0):
    return None
  # Output to files
  roi = crop_minAreaRect(img, mx_rect)
  #cv2.imwrite('gestures/' + str(0) + '.bmp', roi)
  
  return (black_white_pixels.cal(roi), x_y_size.cal(roi))
  