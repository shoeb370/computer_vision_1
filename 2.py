import cv2
image_path = "lena.jpg"
image = cv2.imread(image_path)
#access pixel at (0,0) location
(b,g,r) = image[0,0]
print("Blue, Green, Red values at location(0,0):",(b,g,r))
#manipulate image shown in image 2
image2 = image.copy()
image2[0:100, 0:100] = (255,255,0)
cv2.imshow("My Image", image)
cv2.imshow("Modified Image", image2)
cv2.waitKey(0)