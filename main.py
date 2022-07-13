import cv2
import numpy as np
import time
import PoseModule as pm
from co_msg import sock_client

# Cam number
DEVICE_NUM = 0
# Open cam
cap = cv2.VideoCapture(DEVICE_NUM)
cap.open(0)

# Open PoseModul
detector = pm.poseDetector()

# Define count,dir,pTime
count = 0
dir = 0
pTime = 0

# Cam status
if not cap.isOpened():
   print("Can not open camera,Please Try it again.")
   exit()

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        # Shoulder, Stomach and knee
        Rangle = detector.findAngle(img, 11, 23, 25)
        Langle = detector.findAngle(img, 12, 24, 26)
        
        Rper = np.interp(Rangle, (160, 280), (0, 100))
        Rbar = np.interp(Rangle, (220, 280), (630, 100))
        Lper = np.interp(Langle, (160, 280), (0, 100))
        Lbar = np.interp(Langle, (220, 280), (630, 100))

        color = (255, 0, 255)
        if Lper == 100 and Rper == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 1.0
                cv2.imwrite('photo.jpg',img)
                sock_client()
                dir = 1
        if Lper == 0 and Rper == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 1.0
                cv2.imwrite('photo.jpg',img)
                sock_client()
                dir = 0

        #print(count)
        cv2.putText(img,str(count),(100,300),cv2.FONT_HERSHEY_SIMPLEX,5,(255,0,0),5)
        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(Lbar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(Lper)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

        # Draw bending lines and angle
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.imshow("Loongson", img)
    if cv2.waitKey(1) in [ord('q'), 27]:
            break

