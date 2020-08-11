#to draw a line on image
import cv2
image = cv2.imread("lena.jpg")
print(image.shape) #(512, 512, 3)#(h,w,d)
image2 = image.copy()
#set start and end point
start = (0,0)
end = (image.shape[1],image.shape[0]) #(w,h)
#set a color of line
color = (255,0,0)
#thickness of the line 5
thickness = 5
cv2.line(image2,start, end, color, thickness)
cv2.imshow("Original image", image)
cv2.imshow("Modified image", image2)
cv2.imwrite(".\\images\\line_on_image.jpg",image2)
cv2.waitKey(0)