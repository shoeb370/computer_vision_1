#Contour Detection and Drawing
''' Step include in contour:
1. convert into grayscale
2. binarize the image - any thresholding
3. Apply canny edge detection
4. find all contour
5. draw contour if needed '''
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
#Converting into grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale image", image)

#binarize the image - OSTU 
(T, binarized) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("Binarize image", binarized)

#Use canny function
canny = cv2.Canny(binarized, 0,255)
cv2.imshow("Canny Edges", canny)

#use findcontours
(contours, heirarchy) = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours determined are ", format(len(contours)))

copiedimage = image.copy()
cv2.drawContours(copiedimage, contours, -1, (0,255,0), 2)
cv2.imshow("Contours", copiedimage)
cv2.imwrite(".\\images\\Contour_image.jpg", copiedimage)
cv2.waitKey(0)


''' - cv2.RET_EXTERNAL, determines the type
of contour we are interested in. cv2.RET_EXTERNAL retrieves
the outermost contours only. We can also use cv2.RET_LIST to
retrieve all contours, cv2.RET_COMP and cv2.RET_TREE, to include
hierarchical contours. 
- cv2.CHAIN_APPROAX_SIMPLE, removes the
redundant points and compresses the contour, thereby saving
memory. cv2.CHAIN_APPROAX_NONE stores all points of the contour
(which require more memory to store them).

The output of the cv2.findContours() function is a tuple with the following
items in it:
–– The first item of the tuple is a Python list of all the contours in the
image. Each individual contour is a NumPy array of (x,y) coordinates
of boundary points of the object.
–– The second item of the output tuple is the contour hierarchy'''