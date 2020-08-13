# GLCM Calculation Using the greycomatrix() Function
import numpy as np
import cv2
import matplotlib.pyplot as plt
import skimage.feature as sk
image = cv2.imread("lena.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#calculate glcm of grayscale image
glcm = sk.greycomatrix(image,[2],[0, np.pi/2])
print(glcm) #simply prints the 4D ndarray.




""" greycomatrix(image, distances, angles, levels, symmetric,normed)
distances: This is a list of pixel-pair distance offsets.
angles: This is a list of angles between the pair of pixels. Make sure the angle is a radian and not a degree.
levels: This is an optional parameter and meant for images having 16-bit pixel values. In most cases, we use 8-bit image pixels
that can have values ranging from 0 to 255. For an 8-bit image, the max value for this parameter is 256.
symmetric: This is an optional parameter and takes a Boolean. The value True means the output matrix will be symmetric. The
default is False.
normed: This is also an optional parameter that takes a Boolean. The Boolean True means that each output matrix is normalized
by dividing by the total number of accumulated cooccurrences for the given offset. The default is False.

The greycomatrix() function returns a 4D ndarray. This is the gray-level co-occurrence histogram. The output value P[i,j,d,theta] represents how many times
the gray-level j occurs at a distance d and angle theta from the gray-level j. If the parameter normed is False (which is the default), the output is of type uint32 (a 32-bit
unsigned integer); otherwise, it is float64 (a 64-bit floating point). """
