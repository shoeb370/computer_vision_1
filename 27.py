#Canny Edge Detection
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
#blurr image
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.bilateralFilter(image, 5,50,50)
cv2.imshow("Blurr Image", image)

#Canny function for edge detection
canny = cv2.Canny(image, 50, 170)
cv2.imshow("Canny Edges", canny)
cv2.imwrite(".\\images\\Canny_edge_images.jpg", canny)
cv2.waitKey(0)