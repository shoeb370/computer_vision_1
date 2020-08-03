#Flipping an image
""" The direction of the flip
–– 0 means flip vertically.
–– 1 means flip horizontally.
–– -1 means first flip horizontally and then vertically. """
import numpy as np
import cv2
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)
#Flipped horizontally
flippedhorizontally = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flippedhorizontally)
cv2.imwrite("Flipped_Horizontally.jpg", flippedhorizontally)
#flipped Vertically
flippedVertically = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flippedVertically)
cv2.imwrite("Flipped_Vertically.jpg", flippedVertically)
#Flipped horizontally and then vertically
flippedHV = cv2.flip(image, -1)
cv2.imshow("Flipped HV", flippedHV)
cv2.imwrite("Flipped_HV.jpg", flippedHV)

cv2.waitKey(0)