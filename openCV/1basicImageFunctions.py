import cv2
import matplotlib.pyplot as plt
import numpy as np
img =cv2.imread('resources/girl.jpg')

kernel =  np.ones((5,5), np.uint8)
# by default color sting comes in format BRG to convert it to Standard RGB
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# to convert it to gray
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(img_gray)
#blur a image
imgBlur = cv2.GaussianBlur(img_gray,(7,7),0) # 7,7 is karnel value it should be always odd

cv2.imshow('image',img_gray)
cv2.imshow('blurimage',imgBlur)
# canny function to get edges
imgCanny = cv2.Canny(img,100,100)
cv2.imshow('canny',imgCanny)
# iamge dilation to increase the width of edges
imgDilation = cv2.dilate(imgCanny,kernel,iterations=2)
cv2.imshow('dialtion',imgDilation)
cv2.waitKey(0)