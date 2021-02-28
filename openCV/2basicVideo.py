import cv2
# for feeding static file
cap = cv2.VideoCapture("resources/resource2.mp4")
# for feeding the webcap feed
cap = cv2.VideoCapture(0)
cap.set(3,640) # 3 is width
cap.set(4,480) #4 is height
cap.set(10,100) #100 is brightness
while True:
    success,img = cap.read()
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break