import cv2
import numpy as np

from pathlib import Path

def cal(img):
	n_white_pix = np.sum(img == 255)
 
	return str((img.size-n_white_pix)/n_white_pix)
