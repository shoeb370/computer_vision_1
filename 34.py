import numpy as np
import cv2
import skimage.feature as sk

#load an image
image = cv2.imread("lena.jpg")

#HOG calculation
(HOG, hogimage) = sk.hog(image, orientations=9, pixels_per_cell=(8,8), cells_per_block=(2,2),visualize=True ,block_norm='L2-Hys',transform_sqrt=True,feature_vector=True)

print("Original Image Dimension:", image.shape)
print("Feature Vector Dimension:", HOG.shape)
cv2.imwrite(".\\images\\HOG_image.jpg",hogimage)
#HOG show
cv2.imshow("Original Image", image)
cv2.imshow("HOG Image", hogimage)

cv2.waitKey(0)