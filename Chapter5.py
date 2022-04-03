# #Shapes and text
#
#
# import cv2
# import numpy as np
#
# #black image
# img = np.zeros((512,512,3),np.uint8)
# print(img)
#
# #showing blue color of this size on black img
# img[200:300,100: 300] =255,0,0
# cv2.imshow("Image", img)
# print(img)
# cv2.waitKey(0)






#wrap perspective
import cv2
import numpy as np
img=cv2.imread("C:/Users/PSF/Pictures/leftwing.png")
width,height =250,350
pts1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 448]])
pts2 = np.float32([[0, 0], [width, 0],[0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgoutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Image", img)
cv2.imshow("Output", imgoutput)
cv2.waitKey(0)