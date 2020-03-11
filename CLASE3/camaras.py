import numpy as np
import cv2
cap1=cv2.VideoCapture(0)
cap2=cv2.VideoCapture(1)
#determinar si estan actiadas
print("activado camara 1:",cap1.isOpened())
cap1.release()
print("activado camara 1:",cap1.isOpened())
cap1=cv2.VideoCapture(0)
print("activado camara 1:",cap1.isOpened())

print("activado camara 2:",cap2.isOpened())
print(cap1.get(cv2.CAP_PROP_FPS))
print(cap2.get(cv2.CAP_PROP_FPS))
while True:
    ret1,frame1=cap1.read()
    ret2,frame2=cap2.read()
    cv2.imshow("IMAGEN 1",frame1)
    cv2.imshow("IMAGEN 2",frame2)
    if cv2.waitKey(1)==ord("q"):
        break
        