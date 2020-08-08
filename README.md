# computer_vision_)1
Learn from book building a Computer Vision Applications using Artificial Neural Networks by Shamshad Ansari
Publication Apress



Currently work in progress.
Below here are some list of code that are completed.


## Techniques of Image processing
- Resizing
11. Cropping: Crop the image to get only the face of the lena
- Image Arithematic 
12. Addition of two Images
13. Substraction of two Images
- Bitwise Operation
14. Bitwise Operation
- Masking.
15. Masking Using Bitwise AND Operation
-Splitting and Merginig channel
16. Splitting channel 
17. Merging of all channel
- Noise reduction using smoothing and blurring

Smoothing, also called blurring, is an important image processing technique to reduce noise present in an image 

18. Smoothing/Blurring by Mean Filtering or Averaging

Salt and pepper noise: Contains random occurrences of black and white pixels

Impulse noise: Means random occurrences of white pixels

Gaussian noise: Where the intensity variation follows a Gaussian normal distribution 

19. Smoothing Using the Gaussian Technique

Gaussian filtering is one of the most effective blurring techniques in image processing.
blurring technique gives a more natural smoothing result compared to the averaging technique. 

-- The image represented by the NumPy array.

–– The k×k matrix as the kernel height and width.

–– sigmaX and sigmaY is a standard deviation in the X and Y directions.

20. Median Blurring

The previous three blurring techniques yield blurred images with the side effect that we lose the edges in the image.To blur an image while preserving the edges, we use bilateral
blurring, which is an enhancement over Gaussian blurring.

21. Bilateral blurring.

- Binarization with thresholding

Image binarization is the process of converting a grayscale image into a binary—a black-and-
white—image. We apply a technique called thresholding to binarize an image.

22. Binarization Using Simple Thresholding
23. Binarization Using Adaptive Thresholding

Adaptive thresholding is used to binarize a grayscale image that has a varying degree of pixel intensity, and one single threshold value may not be suitable to extract the information from the image.