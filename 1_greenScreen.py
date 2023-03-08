import cv2
import numpy as np

video = cv2.VideoCapture("sofa.mp4")
image = cv2.imread("sunset.jpg")

while True:

    ret, frame = video.read()
    #print(f'frame size: {frame.shape}')

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    u_green = np.array([29, 46, 26])
    l_green = np.array([74, 121, 49])

    mask = cv2.inRange(frame, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f==0, image, f)

    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    if cv2.waitKey(5) == 27:
        break

video.release()
cv2.destroyAllWindows()
