#Ostu Binarization
# cv2.THRESH_BINARY+cv2.THRESH_OTSU
import numpy as np
import cv2
image = cv2.imread("lena.jpg")

#conevrting it into gray scale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original grayscale image", image)

#Binarize the image using Thresholding
(T, binarizeimage) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Threshold value with ostu's binarization", T)
cv2.imshow("Ostu Binarize image", binarizeimage)
cv2.imwrite(".\\images\\Ostu_image.jpg", binarizeimage)

#Binarization with inverse thresholding
(Ti, inversebinarizeimage) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
print("Threshold value with ostu's inverse binarization", Ti)
cv2.imshow("Ostu Inverse Binarize image", inversebinarizeimage)
cv2.imwrite(".\\images\\Ostu_inverse_image.jpg", inversebinarizeimage)

cv2.waitKey(0)