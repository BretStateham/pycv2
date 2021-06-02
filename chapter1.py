import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)


kernel = np.ones((3,3), np.uint8)

imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)

imgEroded = cv2.erode(imgDialation,kernel, iterations=1)

cv2.imshow("Grayscale",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dialation",imgDialation)
cv2.imshow("Eroded",imgEroded)

cv2.waitKey(0)


