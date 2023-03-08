import cv2

video = cv2.VideoCapture("sofa.mp4")
image = cv2.imread("sunset.jpg")

cv2.namedWindow("Trackbars")
cv2.resizedWindow("rackbars", 300, 300)

cv2.createTrACKBAR("L - V", "Trackbars", 0,aa)
while True:
    ret,frame = video.read()
    frame = cv2.resize(frame, (640,480))
    image = cv2.resize(image, (640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, )
    cv2.imshow("Frame",frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()