#cropping of an Image
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)
# Crop the image to get only the face of the lena
croppedimage = image[50:400, 70:450]
cv2.imshow("Cropped Image", croppedimage)
cv2.imwrite(".\\images\\Croped_Image.jpg", croppedimage)
cv2.waitKey(0)