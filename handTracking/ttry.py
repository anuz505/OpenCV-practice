import cv2
import mediapipe as mp # type: ignore
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ptime = 0
ctime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                if id == 0:
                    cv2.circle(img, (cx,cy), 15, (255, 195, 0), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
           
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255, 195, 0),3)
    cv2.imshow("camera", img)
    cv2.waitKey(1)

