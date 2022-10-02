import mediapipe as mp
import numpy as np
import cv2

myVideo = cv2.VideoCapture(0)

mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4,2)


hand_obj = mp.solutions.hands
hands = hand_obj.Hands()




while True:
    success, frame = myVideo.read()
    frame=cv2.resize(frame,(900,580))
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    handPoints = results.multi_hand_landmarks
    
    guidebox=cv2.imread('guidebox.png')
    guidebox=cv2.resize(guidebox,(250,250))
    alpha=0.4
    
    displayGuide=cv2.addWeighted(frame[0:250,0:250,:],alpha,guidebox[0:250,0:250,:],1-alpha,0)
    frame[0:250,0:250]=displayGuide
    
    

    if handPoints:
        
        handList = []
        for handLms in handPoints:
            mpDraw.draw_landmarks(frame, handLms, hand_obj.HAND_CONNECTIONS)
            for idx, lm in enumerate(handLms.landmark):

                              h, w, c = frame.shape
                              cx, cy = int(lm.x * w), int(lm.y * h)
                              handList.append((cx, cy))

            for point in handList:
                cv2.circle(frame, point, 5, (200,0,200), cv2.FILLED)

        upCount = 0
        for coordinate in finger_Coord:
            if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
                upCount += 1
        if handList[thumb_Coord[0]][0] > handList[thumb_Coord[1]][0]:
            upCount += 1


        print(upCount)
        if(upCount==1):
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if(upCount==2):
            frame,col=cv2.pencilSketch(frame,sigma_s=60,sigma_r=0.07,shade_factor=0.05)
        if(upCount==3):
            frame=cv2.bitwise_not(frame)

        if(upCount==4):
            gr,frame=cv2.pencilSketch(frame,sigma_s=60,sigma_r=0.07,shade_factor=0.05)
        if(upCount==5):
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)             
                          
   
    
        
    

    
    cv2.imshow("hand detect", frame)
   
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    cv2.waitKey(1)

