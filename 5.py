#Create a canvas black image using numpy zero
import cv2
import numpy as np
#create a new canvas
canvas = np.zeros((500,500,3),dtype = "uint8")
canvas2 = canvas.copy()
canvas3 = canvas.copy()
#now we are going to create a rectangle inside numpy zeros
start = (50,50)
end = (200,200)
color = (0,0,255)
thickness = 5 
cv2.rectangle(canvas2, start, end, color, thickness)
thickness = -1 
cv2.rectangle(canvas3, start, end, color, thickness)

cv2.imshow("Original Image", canvas)
cv2.imshow("Modified canvas", canvas2)
cv2.imshow("Modified canvas thickness -1", canvas3)
#Now we are going to save the image
cv2.imwrite(".\\images\\Modified_canvas.jpg",canvas2)
cv2.imwrite(".\\images\\Modified_neg_canvas.jpg",canvas3)
cv2.waitKey(0)