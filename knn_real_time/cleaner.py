import cv2
import numpy as np
import detector

from pathlib import Path

def do(img):
	kernel = np.ones((35,35),np.uint8)
	closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
	
	return detector.do(opening)
	
	
