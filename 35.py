#LBP Image and Histogram Calculation and Comparison with Original Image
import cv2
import numpy as np
import skimage.feature as sk
import matplotlib.pyplot as plt
image = cv2.imread("lena.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orignal Image", image)

#Calculate the histogram of Original Image
originalhist = cv2.calcHist(image, [0], None, [256], [0,256])

plt.figure()
plt.title("Histogram of Original Image")
plt.plot(originalhist, color='red')

#Calculate the LBP of the Original Image
radius = 3
points = 3*8
lbp = sk.local_binary_pattern(image, points, radius, method="default")
lbphist, _ = np.histogram(lbp, density=True, bins=256, range=(0,256))

plt.figure()
plt.title("Histogram of LBP Image")
plt.plot(lbphist, color="green")
plt.savefig(".\\images\\histogram_lbp.jpg", dpi=300, bbox_inches='tight')
plt.show()

#Showing LBP Image
cv2.imshow("LBP images", lbp)
cv2.imwrite(".\\images\\lbp_images.jpg", lbp)
cv2.waitKey(0)