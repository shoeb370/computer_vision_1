#to draw a rectangle on image
import cv2
image = cv2.imread("lena.jpg")
print(image.shape) #(512, 512, 3)#(h,w,d)
image2 = image.copy()
#set start and end point
#top left and bottom right corner
start = (110, 50)
end = (390,400)
#set color and thickness
color = (0,255,0)
thickness = 5
cv2.rectangle(image2, start, end, color, thickness)
cv2.imshow("Original Image", image)
cv2.imshow("Modified Image", image2)
#if you want to save the image 
cv2.imwrite("Modified_rectangle.jpg", image2)
cv2.waitKey(0)