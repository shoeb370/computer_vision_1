import numpy as np
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("lena.jpg")
#now grayscale
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)

#calculate the histogram of grayscale image
hist = cv2.calcHist([image], [0], None, [256], [0,255])

#plot histogram
plt.title("Grayscale Histogram of Orginal Image")
plt.xlabel("Bins")
plt.ylabel("Numbers of Pixels")
plt.plot(hist, color = 'black')
plt.show()

#Now finding equalized image of grayscale image
equalizedimage = cv2.equalizeHist(image)
cv2.imshow("Equalized Image", equalizedimage)
cv2.imwrite(".\\images\\Equalized_image_grayscale.jpg", equalizedimage)

#Now calculating the Histogram of Equalized Image
histequalized = cv2.calcHist([equalizedimage], [0], None, [256], [0,255])

#plot histogram
plt.title("Grayscale Histogram of Equalized Image")
plt.xlabel("Bins")
plt.ylabel("Numbers of Pixels")
plt.plot(histequalized, color = 'black')
plt.savefig(".\\images\\histogram_of_equalized_image.jpg", dpi=300, bbox_inches='tight')
plt.show()

cv2.waitKey(0)