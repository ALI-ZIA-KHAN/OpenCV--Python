
#resizing and cropping

import cv2
import numpy as np
img=cv2.imread("C:/Users/PSF/Pictures/leftwing.png")
print(img.shape)
imgResize = cv2.resize(img, (1000, 600))
#resizing the image width and height ^^
print(imgResize.shape)

imgCropped = img[0:200, 200:500]
#from this height:width to be cropped till that height:width
#img cropped w/o openCV func but diff is it takes height first insted of width like in openCV
cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)
while True:
    if cv2.waitKey(1) & 0XFF ==ord('q'):
     break