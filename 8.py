#Image Translation Along the x- and y-Axes
""" The translation matrix defines the direction
and amount of movement. The warpAffine function is the OpenCV function that does
the actual movement. The cv2.warpAffine function takes three arguments: the image
NumPy, the translation matrix, and the dimension of the image. """
import numpy as np
import cv2
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)
#define translation matrix
translationMatrix = np.float32([[1,0,50],[0,1,20]])
#Move the image
movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1],image.shape[0]))
cv2.imwrite("Moved_Image_translation_matrix.jpg", movedImage)
cv2.imshow("Moved Image", movedImage)
cv2.waitKey(0)
""" The first row, as defined by [1,0,50], represents the movement along the x-axis by
50 pixels to the right. If the third element of this array is a negative number, the
movement will be to the left.
The second row represented by [0,1,20] defines the movement along the y-axis by
20 pixels down. If the third element of this second row is a negative number, this will
move the image up along the y-axis. 
In warpAffine: The last argument is a tuple that has the width and height of the
canvas within which we want to move our image. In this example, we
are keeping the canvas size the same as the original height and width
of the image"""