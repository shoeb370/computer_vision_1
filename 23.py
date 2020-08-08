import cv2
import numpy as np
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)


#convert color image into grayscale image.
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", image2)

# Binarization using adaptive thresholding and simple mean
binarized_mean = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7,3)
#The size of the neighborhood in our example is 7×7
# 3-> A constant value C that will be subtracted from the calculated thresholds
cv2.imshow("Adaptive Threshold using mean", binarized_mean)
cv2.imwrite(".\\images\\adaptive_thres_mean.jpg", binarized_mean)

# Binarization using adaptive thresholding and Gaussian Mean
binarized_gm = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)
cv2.imshow("Adaptive thresholding using gaussian mean", binarized_gm)
cv2.imwrite(".\\images\\adaptive_thres_gaussmean.jpg",binarized_gm)
cv2.waitKey(0)