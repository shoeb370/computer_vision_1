#merging of channel
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)

#splits the image into component color
(b,g,r) = cv2.split(image)

#merged all image 
#if you want to see all image of b,g,r go to 16.py
merged = cv2.merge([b,g,r])
cv2.imshow("Merged Image", merged)
cv2.imwrite(".\\images\\Merged_image.jpg", merged)

cv2.waitKey(0)