import numpy as np
import cv2
image = cv2.imread("lena.jpg")
cv2.imshow("Origial Image", image)
""" Bilateral Filter with
-- The image that needs to be blurred.
–– The diameter of the pixel neighborhood.
–– Color value. A larger value of the color means that more colors of the
neighborhood pixels will be considered when computing the blur.
–– A space or distance. A larger value of the space means that the pixels
farther from the central pixel will be considered. """
filter5 = cv2.bilateralFilter(image, 5, 150, 50)
cv2.imshow("Filtered Image 5",filter5)
cv2.imwrite(".\\images\\bilateral5.jpg",filter5)
#bilateral filter with kernel 7
filter7 = cv2.bilateralFilter(image, 7, 160, 60)
cv2.imshow("Filtered Image 7",filter7)
cv2.imwrite(".\\images\\bilateral7.jpg",filter7)
cv2.waitKey(0)