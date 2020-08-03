#creating a circle inside numpyzeros
import cv2
import numpy as np
#create a new canvas
canvas = np.zeros((512,512,3),dtype = "uint8")
canvas2 = canvas.copy()
mid = 512//2 # creating the mid-point of rectangle
center = (mid, mid)
radius = 100
color = (0,255,255)
thickness = 5
cv2.circle(canvas2, center, radius, color, thickness)
cv2.imshow("Circle canvas", canvas2)
cv2.imwrite("canvas_circle.jpg", canvas2)
cv2.waitKey(0)
