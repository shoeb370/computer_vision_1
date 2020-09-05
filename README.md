# computer_vision_01
Learn from book building a Computer Vision Applications using Artificial Neural Networks by Shamshad Ansari
Publication: Apress

install opencv packages: pip install opencv-python

install numpy packages: pip install numpy

install scikit image packages: pip install scikit-image



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

- Ostu binarization

In the simple thresholding, we select a global threshold that is arbitrarily selected. It is difficult to know what the right value of the threshold is, so we may need to do trial-and-error experiments a few times before you get the right value. Even if you get an ideal value for one case, it may not work with other images that have different pixel intensity
characteristics.

Otsu’s method determines an optimal global threshold value from the image
histogram

24. Ostu's Binarization


### Gradient and Edge Detection
Edge detection involves a set of methods to find points in an image where the brightness of pixels changes distinctly.

- Sobel Derivatives(cv2.Sobel() function)

The Sobel method is a combination of Gaussian smoothing and Sobel differentiation, which computes an approximation of the gradient of an image intensity function. Because of the Gaussian smoothing, this method is resistant to noise.

25. Sobel and Schar Gradient Detection

- Note: A data type, cv2.CV_64F, which is a 64-bit float. Why? The transition from black-to-white is considered a positive slope, while the transition from white-to-black is a negative slope. An 8-bit unsigned integer cannot hold a negative number. Therefore, we need to use a 64-bit float; otherwise, we will lose gradients when the transition from white to black happens.

- Laplacian Derivatives (cv2.Laplacian() Function)

The Laplacian operator calculates the second derivative of the pixel intensity function to
determine the edges in the image.

26. Edge Detection Using Laplacian Derivatives
- Canny Edge Detection
Canny edge detection is one of the most popular edge detection methods in image processing. This is a multistep process. It first blurs the image to reduce noise and then computes Sobel gradients in the X and Y directions, suppresses the edges where nonmaxima is calculated, and finally determines whether a pixel is “edge-like” or not by applying hysteresis thresholding.
27. Canny Edge Detection
- Contours: Contours are curves joining continuous points of the same intensity. Determining contours is useful for object identification, face detection, and recognition.
28. Contour Detection and Drawing

## Building a Machine Learning- Based Computer Vision System

- Calculate the histogram of the image.

29. Histogram of a Grayscale Image
30. Histogram of Three Channels of RGB Color Image
- Histogram Equalizer
Histogram equalization is an image processing technique to adjust the contrast of an image. It is a method of redistributing the pixel intensities in such a way that the intensities of the under-populated pixels are equalized to the intensities of over-populated pixel intensities
31. Histogram Equalization
- GLCM
The gray-level co-occurrence matrix (GLCM) is the distribution of simultaneously occurring pixel values within a given offset. An offset is the position (distance and direction) of adjacent pixels. As the name implies, the GLCM is always calculated for a grayscale image.
32. GLCM Calculation Using the greycomatrix() Function
the GLCM is not directly used as a feature, but we use this to calculate some useful statistics, which gives us an idea about the texture of the image. 

Contrast - Measures the local variations in the GLCM.
Correlation - Measures the joint probability occurrence of the specified pixel pairs.
Energy - Provides the sum of squared elements in the GLCM. Also known as uniformity or the angular second moment
Homogeneity - Measures the closeness of the distribution of elements in the GLCM to the GLCM diagonal.

33. Calculation of Image statistic from the GLCM

- HOG: Histogram of Oriented gradient
important feature description for object detection
structural shape and appearance of an object in an image
The HOG algorithm computes the occurrences of gradient orientation in localized portions of the image.

34. Program to built HOG

- LBP: Local binary patterns

35. LBP Image and Histogram Calculation and Comparison with Original Image

## Feature Selection

Feature selection is the process of selecting variables or attributes that are relevant and useful in model training. This is a process of eliminating unnecessary or irrelevant features and selecting a subset of features that are strong contributors to the learning of the model.

Feature Extraction - Process of creating Feature

Feature Selection - Process of removing unecessary feature
- Filter Method: Filtering is a process that allows you to do preprocessing to select the feature subset. In this process, you determine a correlation between a feature and the target variable and determine their relationship based on statistical scores.

- Wrapper Method:In the wrapper method, you use a subset of features and train the model. Evaluate the model, and based on the result, either add or remove features and retrain the model. 1. Forward Selection, 2. Backward Elimination, 3. Recursive Feature Elimination

### Model Deployment

- Embedded Model: Edge Computing Device (IoT)
- Model Deployed as seperate service: The model is wrapped. Servic is independentlty deployed and seperated from consuming applications. This allow us to update the model and redeploy them without affecting other applications.
- Model deployed as RESTful web service: Model are called via RESTful API using TCP/IP protocol.
provide scalability and Load balancing.
- Model Deployed for distributed process: Highly scalable model deployment. Input image stored in distributed storage that is accessible by all nodes of a cluster. All participanting nodes takes input from distributed storage, process them and stored the prediction outcome to distributed storage for application to consuming. eg. Hadoop Distributed File System (HDFS), Amazon S3, Google Cloud storage and Azure Blob Storage. 

## Chapter 5: Deep Learning and Artificial Neural Networks (ANN):

An ANN is a computing system that is designed to work the way human brain works. 
A human body has a billions of neurons with trillions interconnections amongs them. These interconnected neurons are called as neural network.

![Human Neurons](https://cdn1.byjus.com/wp-content/uploads/2020/02/STRUCTURE-OF-NEURON.png)

Computer scientists were inspired by the human vision system and tried to mimic
neural networks by creating a computer system that learns and functions the way our
brains do. This learning system is called an artificial neural network (ANN).
![Artificial Neurons](https://cdn-images-1.medium.com/freeze/max/1000/1*tMuOsWWRX3fR84xoSeJcAw.png?q=20)
The variable x1, x2,...xn are the input signal(image features) with certain weight w1, w2,...wn associated with each input signal. These input signal processed using some mathematical functions to generate outputs. The processing unit combine with these inputs signal is called neurons. The mathematical function that computes the output from the neuron is called an activation function. the circle matks with sigma symbol is the neuron. the output y is generated from the neuron.
