#joining images
import cv2
import numpy as np
img = cv2.imread("C:/Users/PSF/Pictures/leftwing.png")
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
#images must be of same no of channels

cv2.imshow("Vertical",imgVer)
cv2.imshow("Horizontal", imgHor)
cv2.waitKey(0)


#left one part