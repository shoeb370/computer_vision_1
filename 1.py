#demosntrating the simple opencv function and key concept
import cv2
image_path = "lena.jpg"
image = cv2.imread(image_path)
print("Dimension",image.ndim)
print("image height:", image.shape[0])
print("image width:", image.shape[1])
print("image channel/Depth:",image.shape[2])
print("Size of an array: ", image.size)
cv2.imshow("My Image", image)
cv2.waitKey(0)