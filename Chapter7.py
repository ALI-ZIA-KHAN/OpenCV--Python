#COLOR DETECTION



#first we made tracbars after converting img into hsv
#initially trackbars had starting and ending values for h s and v
#then after setting all 6 of them we get 6 values(we kept the color we want to detect as white color in masking)
#then put this as initial pint of rackbars(as of now)
#now in order to get actual clr inplace of white clr we used to create a new image with bitwise and
#it compare original img with masked one, and wherever it sees 1 on both sides it will be true for that point

import cv2
import numpy as np

def empty(a):
    pass


path="C:/Users/PSF/Pictures/leftwing.png"
img = cv2.imread(path)

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min", "TrackBars",8,179, empty)
cv2.createTrackbar("Hue Max","TrackBars",123,179, empty)
cv2.createTrackbar("Sat Min", "TrackBars",0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars",169, 255, empty)
cv2.createTrackbar("Vue Min","TrackBars",13,255, empty)
cv2.createTrackbar("Vue Max","TrackBars",255,255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min =cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Vue Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Vue Max", "TrackBars")
    print(h_min, h_max,s_min, s_max, v_min,v_max)
    lower = np.array([h_min, s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHSV,lower,upper)
    imgResult=cv2.bitwise_and(img,img, mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Iammask",mask)
    cv2.imshow("imgResult",imgResult)
    cv2.waitKey(1)