#Addition of an Image
#Each pixel in an image can have integer value between 0-255
#So 230+ 30 = 255
""" cv2.add(): which takes the two equal-sized images as arguments and
adds their pixel values to produce the result.
cv2.addWeighted(): which is generally used for blending two
images. More details about this function are provided in a moment """
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
#Now addition of two image
resultant = cv2.add(resizedimage1,resizedimage2)
cv2.imshow("Resultant Image add(a,b)", resultant)
cv2.imwrite(".\\images\\Addition_Image.jpg", resultant)
#weighted addition
weightedimage = cv2.addWeighted(resizedimage1,0.7,resizedimage2,0.3,0)
cv2.imshow("Weighted_image",weightedimage)
cv2.imwrite(".\\images\\Weighted_add.jpg",weightedimage)
#Enhance Image
imageenhanced = 255*resizedimage1
cv2.imshow("Enhance Image", imageenhanced)
cv2.imwrite(".\\images\\Enhanced_Image.jpg",imageenhanced)
arrayimage = resizedimage1+resizedimage2
cv2.imshow("Array Image(a+b)", arrayimage)
cv2.imwrite(".\\images\\Array_image_add.jpg",arrayimage)
cv2.waitKey(0)
""" ResultantImage = α x image1 + β x image2 + γ 
where 𝝰 is the weight of image 1, 𝛃 is the weight of image 2, and 𝛄 is a constant. By
varying the values of these weights, we create the desired effects of additions. """