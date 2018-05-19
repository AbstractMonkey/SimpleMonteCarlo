import cv2
from matplotlib import pyplot as plt
from random import randint
import copy

# Pull in .png image
circle_img = cv2.imread('test.png',0)

# Get and print height and width of the image
img_height, img_width = circle_img.shape
print(circle_img.shape, circle_img.dtype)

# Make a copy for graphical imaging purposes
#circle_img[img_height-1,:] = 255
circle_img_copy = copy.copy(circle_img)

# Set up variables for the MonteCarlo algorithm loop
CountPixelW = 0
CountPixelB = 0
counter = 0

while counter < 300000:
    ycoord = randint(0,img_height-1)
    xcoord = randint(0,img_width-1)
    circle_img_copy[ycoord,xcoord]=100
    if circle_img[ycoord,xcoord]==255:
        CountPixelW+=1
        counter+=1
    else:
        CountPixelB+=1
        counter+=1
        
plt.suptitle('MonteCarlo Algorithm Demonstration', fontsize=16)
plt.ylabel('pixels')
plt.xlabel('pixels')
plt.imshow(circle_img_copy)

print("There were " + str(CountPixelB) + " black pixels and " + str(CountPixelW) + " white pixels randomly landed on")
print(str((CountPixelB/(CountPixelW + CountPixelB))*100) + "% of this image is consumed by area of the object")
