#Histogram of a Grayscale Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

#read image and convert it into grayscale
image = cv2.imread("lena.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image", image)

#calculate histogram 
hist = cv2.calcHist([image], [0], None, [256], [0,255])

#plot histogram graph
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")
plt.plot(hist, color = 'black')
plt.savefig('.\\images\\hist_grayscale_plot.jpg', dpi=300, bbox_inches='tight')
plt.show()
#Saving an plot as image

cv2.waitKey(0)






""" calcHist(images, channels, mask, histSize, ranges, accumulate)
This function takes the following arguments:
images: This is a NumPy array of image pixels. If you have only
one image, just wrap the NumPy variable within a pair of square
brackets, e.g., [image].
channels: This is an array of indexes of channels we want to
calculate the histogram for. This will be [0] for grayscale images
and [0,1,2] for RGB color images.
mask: This is an optional argument. If you do not supply a mask,
the histogram will be calculated for all the pixels in the image or
images. If you supply a mask, the histogram will be calculated for
the masked pixels only.
histSize: This is the number of bins. If we pass this value as
[64,64,64], this means that each channel will have 64 bins. The bin
size may be different for different channels.
ranges: This is the range of pixel values, which is normally [0,255]
for grayscale and RGB color images. This value may be different in
other color schemes, but for now, let’s stick to RGB only.
accumulate: This is the accumulation flag. If it is set, the histogram
is not cleared in the beginning when it is allocated. This feature
enables you to compute a single histogram from several sets of
arrays or to update the histogram in time. The default value is None. """