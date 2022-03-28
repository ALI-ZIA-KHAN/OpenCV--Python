# import cv2
# print("hello world imported")
#
# img =cv2.imread("C:/Users/PSF/Pictures/leftwing.png")
# #function to take img for reading
# cv2.imshow("Output",img)
# #to show img in "Output" window
# cv2.waitKey(0)
# #to wait infinitely to show img



#video playing since its a sequence of images basically so it can be done using while loop
# cap =cv2.VideoCapture("C:/Users/PSF/Videos/Captures/newvideo.mp4")
# while True:
#     success, img = cap.read()   #success is variable which will hold boolean value
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0XFF ==ord('q'):   #condition to stop video only when pressed a 'q'
#      break



# import cv2
# id of camera
# cap =cv2.VideoCapture(1)
#height id is 3
# cap.set(3,640)
# width id is 4
# cap.set(4,480)
#10 is brightness id
# cap.set(10,100)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0XFF ==ord('q'):
#      break
#webcam video^^




import cv2
import numpy as np

img = cv2.imread("C:/Users/PSF/Pictures/leftwing.png")
kernel=np.ones((5,5),np.uint8)
print("kernel",kernel)


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#making img gray
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
#making img blur
imgCanny=cv2.Canny(img,100,200)
#identifying edges values given are of threshold

imgDialation=cv2.dilate(imgCanny,kernel,iterations=1)
#GETTING EDGES THICK of the image more iteration more thick

imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
#opposite of dilating

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialated Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)

while True:
    if cv2.waitKey(1) & 0XFF ==ord('q'):
     break