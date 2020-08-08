import cv2
import numpy as np
image1 = cv2.imread("lena.jpg")
image2 = cv2.imread("HappyFish.jpg")
cv2.imshow("Origianl 1",image1)
cv2.imshow("Orignal 2", image2)
print(f"size of image1: {image1.shape},\nsize of image2: {image2.shape}")
#note for doing arithematic operation size of image should be same
resizedimage1 = cv2.resize(image1,(300,300),interpolation=cv2.INTER_AREA)
resizedimage2 = cv2.resize(image2,(300,300),interpolation=cv2.INTER_AREA)
#Substract image2-image1
subs1 = cv2.subtract(resizedimage2,resizedimage1)
cv2.imshow("subs1: sub(2-1)", subs1)
cv2.imwrite(".\\images\\Substract1.jpg",subs1)
#Substract image2-image1
subs2 = cv2.subtract(resizedimage1,resizedimage2)
cv2.imshow("subs1: sub(1-2)", subs2)
cv2.imwrite(".\\images\\Substract2.jpg",subs2)
#Numpy Substraction Image2 - Image1
subs3 = resizedimage2-resizedimage1
cv2.imshow("Numpy Substract 2-1", subs3)
cv2.imwrite(".\\images\\Substract3.jpg",subs3)
#A constant Substraction
subs4 = resizedimage1-50
cv2.imshow("Constant substract from and image", subs4)
cv2.imwrite(".\\images\\Substract4.jpg",subs4)
cv2.waitKey(0)
