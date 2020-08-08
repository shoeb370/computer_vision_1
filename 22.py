import cv2
import numpy as np
image = cv2.imread("lena.jpg")
cv2.imshow("Orignal Image", image)

#convert color image into grayscale image.
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", image2)
cv2.imwrite(".\\images\\Grayscale_image.jpg", image2)

#Binarize the image using thresholding
(T, binarizeimage) = cv2.threshold(image2, 100, 255, cv2.THRESH_BINARY)
""" (image,T-threshold value,The max value that will be set if the pixel value is greater than the threshold,A thresholding method such as cv2.THRESH_BINARY or cv2.THRESH_ BINARY_INV)
"""
cv2.imshow("Binarize Image", binarizeimage)
cv2.imwrite(".\\images\\binarize_100_image.jpg",binarizeimage)

#binarization with inverse thresholding
(Ti, inversebinarizeimage) = cv2.threshold(image2, 100, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse binarize image ", inversebinarizeimage)
cv2.imwrite(".\\images\\ineversebinarize_100.jpg", inversebinarizeimage)
cv2.waitKey(0)