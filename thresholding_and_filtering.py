# -*- coding: utf-8 -*-
"""Thresholding_and_Filtering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OzEIBpF1awZdg-7u4ls0G_dOACqr6CxC
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread("/content/cameraman.tif",0) #reading the image

#Original Image
plt.imshow(img,cmap="gray")

#finding the grey level of the image
import math
Nimg=np.copy(img)
max_level=Nimg.max()
k=round(math.log(max_level,2))
L=2**k

nrows,ncols=Nimg.shape  #storing no. of rows,cols of the img array in variables

"""###**Task A**

####1. Image Negative:
"""

N1img=np.zeros((nrows,ncols))
for i in range(nrows):
  for j in range(ncols):   
     N1img[i,j]=L-1-Nimg[i,j]  #inverting the image that is for pixel 0 in original image it will be L-1 in the negative image.

plt.imshow(N1img,cmap="gray")

"""####2. Thresholding:"""

n=int(input("Enter Threshold value:"))
N2img=np.zeros((nrows,ncols))
for i in range(nrows):
  for j in range(ncols):
    if Nimg[i,j]>n: #L-1 pixels in the thresholded image for pixels greater than the threhold value in the original image and 0 for the rest
     N2img[i,j]=L-1
    else:
       N2img[i,j]=0

plt.imshow(N2img,cmap="gray")

"""####3. Grey Level Slicing(without background):"""

a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
N3img=np.zeros((nrows,ncols))
for i in range(nrows):
  for j in range(ncols):
    if Nimg[i,j]>a and Nimg[i,j]<b: #L-1 pixels in the thresholded image for pixels in the given range(a,b) of the original image and 0 for the rest
     N3img[i,j]=L-1
    else:
       N3img[i,j]=0

plt.imshow(N3img,cmap="gray")

"""####4. Grey Level Slicing(with background):"""

a=int(input("Enter A value:"))
b=int(input("Enter B value:"))
N4img=np.zeros((nrows,ncols))
for i in range(nrows):
  for j in range(ncols):   #L-1 pixels in the thresholded image for pixels greater than the threhold value in the original image and same as the original for the rest
    if Nimg[i,j]>a and Nimg[i,j]<b:
     N4img[i,j]=L-1
    else:
       N4img[i,j]=Nimg[i,j]

plt.imshow(N4img,cmap="gray")

"""###**Task B**

####Low Pass Filtering
"""

#Low Pass Spatial Domain Filtering to observe the blurring effect
img1= cv2.imread('Test.tif',0)                #reading the image
row,col=img1.shape                             #storing no. of rows,cols of the img array in variables

plt.imshow(img1,cmap="gray")

#Developing Averaging filter (3,3) mask

mask= np.ones([3,3],dtype=int)    #creating initial array of 1's
mask=mask/9
print(mask)

#Convolve/Correlation the 3X3 mask over the image 

img_blur=img1.copy()
for i in range(1,row-1):
    for j in range(1,col-1):
        temp= img1[i-1,j-1]*mask[0,0]+img1[i-1,j]*mask[0,1]+img1[i-1,j+1]*mask[0,2]+img1[i,j-1]*mask[1,0]+img1[i,j]*mask[1,1]+img1[i,j+1]*mask[1,2]+img1[i+1,j-1]*mask[2,0]+img1[i+1,j]*mask[2,1]+img1[i+1,j+1]*mask[2,2]
      
        img_blur[i,j]=temp
#img_new=img_new.astype(np.uint8)
cv2.imwrite('blurred.png',img_blur)

#Blurred image with 3x3 Mask
plt.imshow(img_blur,cmap="gray")

# Spatial domain low pass filtering for a variable size mask
img_blur1= np.zeros([row,col], dtype=int)
b= int(input("Enter size of the mask: "))
a=b//2

for i in range(1,row-a):
    for j in range(1,col-a):
        temp= img1[i-a:i+a,j-a:j+a] 
        
        constant= np.sum(temp)
        img_blur1[i,j]= constant//b**2

#Variable Mask blurred image
plt.imshow(img_blur1,cmap="gray" )

! jupyter nbconvert --to html I078_SIP_Prac4.ipynb

"""##**Conclusion:**
**Task 1:** Performed image negative,thresholding and grey level slicing on an image. 

Image negative basically inverts the pixels in the original image i.e light appears dark and vice versa.

Image Thresholding is basically converting grayscale image into a binary image i.e black and white one. It makes image analysis easier.

Image grey level slicing manipulates a given range of pixels and either diminishes or keeps the remaining pixels same.

**Task 2:** Perfomed low pass filtering and applied blurr effect on an image.Low pass filteriNg smoothens the image i.e removes the high level pixels.
Generated a 3*3 mask and applied it to the original image. ALso applied a variable mask and created similar blur effect.

"""