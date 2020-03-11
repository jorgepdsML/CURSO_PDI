import cv2
import time
cam=cv2.VideoCapture(0)
t1=time.time()
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
video_=cv2.VideoWriter("jorge_video_opencv.avi",fourcc,20.0,(640,480))
while True:
    #esperar 15 segundos o que se haya presionado la tecla 'q'
    if (time.time()-t1)>15 or cv2.waitKey(1)==ord('q'):
        break
    ret,frame=cam.read()
    cv2.imshow("IMAGEN ",frame)
    video_.write(frame)
cam.release()
video_.release()
cv2.destroyAllWindows()