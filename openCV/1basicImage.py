import cv2
#print("success")
# to read images use functiom imread
img = cv2.imread("resources/girl.jpg")
#use imshow to display the images
cv2.imshow("output",img)
# fordelay of the screen 0 means infinite delay 1000 means 1sec
cv2.waitKey(0)