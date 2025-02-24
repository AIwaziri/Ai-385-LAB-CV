import cv2
import numpy as np

# Load the image
image = cv2.imread('Img 2.png')


#part 1
sobelx=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
sobely=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
sobelxy=cv2.Sobel(image,cv2.CV_64F,1,1,ksize=5)

cv2.imshow('Original Image',image)
cv2.waitKey(0)
cv2.imshow('Sobel X',sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y',sobely)
cv2.waitKey(0)
cv2.imshow('Sobel XY',sobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()


# next try with canny

edges = cv2.Canny(image,100,101)
cv2.imshow('Original Image',image)
cv2.waitKey(0)
cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# try harris corner
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
har = cv2.cornerHarris(gray,2,9,0.04)
cv2.dilate(har,None)
image[har>0.01*har.max()]=[0,0,255]
cv2.imshow('Original Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

