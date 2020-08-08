''' Smoothing, also called blurring, is an important image processing technique to reduce noise present in an image '''
''' Salt and pepper noise: Contains random occurrences of black and white pixels
Impulse noise: Means random occurrences of white pixels
Gaussian noise: Where the intensity variation follows a Gaussian normal distribution '''
# Smoothing/Blurring by Mean Filtering or Averaging
import cv2 
import numpy as np
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)

#define kernel 3X3
kernel = (3,3)
blur3x3 = cv2.blur(image, kernel)
cv2.imshow("Blurred Image 3X3",blur3x3)
cv2.imwrite(".\\images\\Blur3x3kernal.jpg",blur3x3)

#kernel 5X5
blur5x5 = cv2.blur(image,(5,5))
cv2.imshow("Blurred 5x5 Image", blur5x5)
cv2.imwrite(".\\images\\Blur5x5kernal.jpg",blur5x5)

#kernel 7X7
blur7x7 = cv2.blur(image,(7,7))
cv2.imshow("Blurred 7x7 Image", blur7x7)
cv2.imwrite(".\\images\\Blur7x7kernal.jpg",blur7x7)

cv2.waitKey(0)