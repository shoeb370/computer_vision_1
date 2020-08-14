import cv2
import numpy as np
import skimage.feature as sk
image = cv2.imread("lena.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original image", image)
#Calculate the glcm of grayscale image
glcm = sk.greycomatrix(image, [2], [0, np.pi/2])

#calculate contrast
contrast = sk.greycoprops(glcm)
print("Contrast: ", contrast)

#Calculate dissimilarity
dissimilarity = sk.greycoprops(glcm, prop="dissimilarity")
print("Dissimilarity: ", dissimilarity)

#Calculate ASM
ASM = sk.greycoprops(glcm, prop="ASM")
print("ASM: ",ASM)

#Calculate ENERGY
energy = sk.greycoprops(glcm, prop="energy")
print("ENERGY: ", energy)

#Calculate Correlation
corr = sk.greycoprops(glcm, prop="correlation")
print("Correlation: ", corr)
cv2.waitKey(0)