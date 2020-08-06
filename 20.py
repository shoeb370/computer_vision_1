#Median Blurring
''' Median blurring is an effective technique for reducing salt-and-pepper type of noise. '''
import numpy as np
import cv2
image = cv2.imread("salt.png")
cv2.imshow("Original Salt Pepper Image", image)

#median filtering for noise reduction
medimage = cv2.medianBlur(image, 3)
cv2.imshow("Median Blur image 3", medimage)
cv2.imwrite("med_blur_3.jpg",medimage)

#medblur5
medimage5 = cv2.medianBlur(image, 5)
cv2.imshow("Median Blur 5 image", medimage5)
cv2.imwrite("Med_blur_5.jpg",medimage5)

cv2.waitKey(0)