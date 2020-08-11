#Edge Detection Using Laplacian Derivatives
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
#now cnverting to Grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#now smoothing
image = cv2.bilateralFilter(image, 5,50,50)
cv2.imshow("blurr original Image", image)

#Laplace function
laplace = cv2.Laplacian(image, cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))
''' - Note: A data type, cv2.CV_64F, which is a 64-bit float. Why? The transition from black-to-white is considered a positive slope, while the transition from white-to-black is a negative slope. An 8-bit unsigned integer cannot hold a negative number.
 Therefore, we need to use a 64-bit float; otherwise, we will lose gradients when the transition from white to black happens.
'''
cv2.imshow("Laplacian Edge", laplace)
cv2.imwrite(".\\images\\Laplacian_edge_image.jpg", laplace)

cv2.waitKey(0)