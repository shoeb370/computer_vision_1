#Sobel and Schar Gradient Detection
import numpy as np
import cv2
""" The Sobel() function also takes an argument ksize that we use to define the kernel size. 
If we set ksize to -1, OpenCV will internally apply a 3×3 Schar filter, 
which generally gives a better result compared to the 3×3 Sobel filter """
image = cv2.imread("lena.jpg")
cv2.imshow("Original Images", image)
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", image2)
image3 = cv2.bilateralFilter(image2, 5, 50, 50)
cv2.imshow("blurr image", image3)

#Sobel Gradient detection
sobelx = cv2.Sobel(image3, cv2.CV_64F, 1, 0, ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
sobely = cv2.Sobel(image3, cv2.CV_64F, 0, 1, ksize=3)
sobely = np.uint8(np.absolute(sobely))

cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imwrite(".\\images\\Sobel_x_image.jpg",sobelx)
cv2.imwrite(".\\images\\Sobel_y_image.jpg",sobely)

#Schar gradient Detection by passing ksize = -1
scharx = cv2.Sobel(image3, cv2.CV_64F, 1, 0, ksize=-1)
scharx = np.uint8(np.absolute(scharx))
schary = cv2.Sobel(image3, cv2.CV_64F, 0, 1, ksize=-1)
schary = np.uint8(np.absolute(schary))
cv2.imshow("Schar X", scharx)
cv2.imshow("Schar Y",schary)
cv2.imwrite(".\\images\\Schar_x_image.jpg",scharx)
cv2.imwrite(".\\images\\Schar_y_image.jpg",schary)

cv2.waitKey()