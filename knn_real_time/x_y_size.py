import cv2
import numpy as np

from pathlib import Path

def cal(img):
	height, width = img.shape[:2]
	
	if height < width:
		return str(height/width)	
	else:
		return str(width/height)
