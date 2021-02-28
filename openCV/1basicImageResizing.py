import cv2

img = cv2.imread("resources/girl.jpg")
# size of image(h,w,no ofchannels eg:BGR)
print(img.shape)
# to resize use resize function wiht perimeter (w,h)
imgNew = cv2.resize(img,(100,100))
cv2.imshow("output",img)
cv2.imshow("new",imgNew)
# croping a image
cropped_image = img[50:170, 150:250] # [height fm:to, width fm:to]
cv2.imshow("cropped", cropped_image)
cv2.waitKey(0)