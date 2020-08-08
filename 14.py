#Bitwise Operation 
import cv2
import numpy as np
#create a white circle using np.zeros
circle = cv2.circle(np.zeros((200,200,3),dtype="uint8"),(100,100), 90, (255,255,255), -1)
#cv2.circle(image, pos, rad, color, thickness)
cv2.imshow("White circle", circle)
cv2.imwrite(".\\images\\numpy_circle.jpg",circle)
#create a square
# create a square
square = cv2.rectangle(np.zeros((200,200,3), dtype= "uint8"), (30,30), (170,170),(255,255,255), -1)
cv2.imshow("White Square", square)
cv2.imwrite(".\\images\\Numpy_square.jpg", square)
#Bitwise AND
bitand = cv2.bitwise_and(square,circle)
cv2.imshow("Bitwise AND image",bitand)
cv2.imwrite(".\\images\\Bitwise_and.jpg",bitand)
#bitwise OR
bitor = cv2.bitwise_or(square,circle)
cv2.imshow("Bitwise OR image",bitor)
cv2.imwrite(".\\images\\Bitwise_or.jpg",bitor)
#bitwise XOR
bitxor = cv2.bitwise_xor(square,circle)
cv2.imshow("Bitwise_XOR image", bitxor)
cv2.imwrite(".\\images\\Bitwise_xor.jpg", bitxor)
#bitwise NOT
bitnot_sq = cv2.bitwise_not(square)
bitnot_circle = cv2.bitwise_not(circle)
cv2.imshow("Bitwise NOT square image",bitnot_sq)
cv2.imwrite(".\\images\\Bitwise_not_square.jpg",bitnot_sq)
cv2.imshow("Bitwise NOT circle image", bitnot_circle)
cv2.imwrite(".\\images\\Bitwise_not_circle.jpg",bitnot_circle)
cv2.waitKey(0)
