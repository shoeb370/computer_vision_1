#Masking
""" Masking refers to the “hiding” or “filtering” of an image. """
#Masking Using Bitwise AND Operation
import cv2
import numpy as np
image = cv2.imread("lena.jpg")
cv2.imshow("Original Image", image)
#now create a rectangular mask
maskimg= cv2.rectangle(np.zeros(image.shape[:2], dtype="uint8",), (50,50), (int(image.shape[1])-50, int(image.shape[0] / 2)-50),(255,255,255),-1)
cv2.imshow("Mask Image",maskimg)
cv2.imwrite(".\\images\\Masked_image.jpg",maskimg)
#Using bitwise_and operation perform masking. Notice the mask=maskImage argument
masked = cv2.bitwise_and(image,image, mask = maskimg)
cv2.imshow("Masked Output",masked)
cv2.imwrite(".\\images\\Masked_output_image.jpg",masked)
cv2.waitKey(0)