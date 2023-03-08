import cv2
import numpy as np

video = cv2.VideoCapture("sofa-11294.mp4")
image = cv2.imread("sunset-g9d1b19c70_1920.jpg")

while True:

    ret, frame = video.read()
    #print(f'frame size: {frame.shape}')

    image = cv2.resize(image, (1920, 1080))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    u_green = np.array([104, 153, 70])
    l_green = np.array([30,30,0])

    mask = cv2.inRange(frame, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f==0, image, f)

    cv2.imshow("video", frame)
    cv2.imshow("mask", f)

    if cv2.waitKey(25) == 27:
        break

video.release()
cv2.destroyAllWindows()
