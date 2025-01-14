import cv2
import numpy as np
cap=cv2.VideoCapture("Ball_Tracking.mp4")
while (True):
    _, frame=cap.read()
    new_image=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower=np.array([36, 25, 25])
    upper=np.array([70, 255,255])

    mask=cv2.inRange(new_image, lower, upper)
    contours,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)>600:
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w, y+h),(0,255,0),2)
    
    res=cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('res', frame)
    cv2.imshow('res', res)
    k=cv2.waitKey(10)
    if k==27:
        break
cv2.destroyAllWindows()
