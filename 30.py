#Histogram of Three Channels of RGB Color Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)

#color in BGR sequences
colors = ("blue", 'green', 'red')
for i , color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [32], [0,256])
    #plot histogram
    plt.plot(hist, color = color)

plt.title("RGB color histogram")
plt.xlabel("Bins")
plt.ylabel('Number of Pixels')
plt.savefig(".\\images\\RGB_image_hist.jpg", dpi=300, bbox_inches='tight')
plt.show()

cv2.waitKey(0)