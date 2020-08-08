# Smoothing Using the Gaussian Technique
''' Gaussian filtering is one of the most effective blurring techniques in image processing.
blurring technique gives a more natural smoothing result compared to the averaging technique. 
-- The image represented by the NumPy array.
–– The k×k matrix as the kernel height and width.
–– sigmaX and sigmaY is a standard deviation in the X and Y directions.'''
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)
# Gaussian blurring with 5x5 kernel and 0 for standard deviation to calculate from the kernel
gaussimage = cv2.GaussianBlur(image, (5,5),0)
cv2.imshow("Gaussian Blurr Image", gaussimage)
cv2.imwrite(".\\images\\Gaussian_blur_image.jpg",gaussimage)
cv2.waitKey(0)