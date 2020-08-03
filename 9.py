# Rotation of Image
# cv2.getRotationMatrix2D
import numpy as np
import cv2
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)
(h,w) = image.shape[:2]
#define translationmatrix
center = (h//2, w//2)
angle = -45
scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
#rotate the image
rotatedImage = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0])) 
cv2.imshow("Rotated Image", rotatedImage)
cv2.imwrite("Rotated_Image.jpg", rotatedImage)
cv2.waitKey(0)