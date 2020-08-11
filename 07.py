#image resizing with respect to aspect ration
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
#get an image height and weight by using image shape function
# (h, w, c) = image.shape[:]
(h,w) = image.shape[:2]
#now to find the aspect ratio
aspect_ratio = w/h
# lets resize the image to decrease height by half of the original image.
#all of the data should be integer format
height = int(0.5*h)
width = int(height * aspect_ratio)
#now we are storing a new dimension in form of tuple
dimension = (height, width)
resize_image = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
""" INTER_AREA: The calculation of the pixel value is performed by
using the pixel area relation (as described by the OpenCV official
documentation). We use this algorithm to create a moiré-free resized
image """
cv2.imshow("Original Image",image) #display original Image
cv2.imwrite(".\\images\\Resized_image.jpg", resize_image) #save the resize image
cv2.imshow("Resized Image", resize_image) #display the resize image
#Resize using x and y factor
resize_with_factor = cv2.resize(image, None, fx = 1.2, fy= 1.2, interpolation= cv2.INTER_LANCZOS4)
""" The third and fourth arguments, fx and fy, are the resize factors
in the horizontal (widthwise) and vertical (heightwise) directions.
These two arguments are optional. """
#INTER_LANCZOS4: This uses the 8×8 nearest neighbor interpolation.
cv2.imwrite(".\\images\\Resized_with_factor.jpg", resize_with_factor)
cv2.imshow("Resized with Factor", resize_with_factor) # original image size increases
cv2.waitKey(0)
