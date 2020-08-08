#Splitting and Merging channels
import cv2
import numpy as np
#load the image
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)
#splits the image into component color
(b,g,r) = cv2.split(image)
cv2.imshow("Blue Image", b)
cv2.imwrite(".\\images\\blue_split_image.jpg",b)
cv2.imshow("Green Image",g)
cv2.imwrite(".\\images\\Green_split_image.jpg",g)
cv2.imshow("Red Image", r)
cv2.imwrite(".\\images\\Red_split_image.jpg",r)
cv2.waitKey(0)