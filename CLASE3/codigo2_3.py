#codigo para registrar un video utilizando opencv y el modulo time
import numpy as np
import cv2
import time
#sleep() pertenece al modulo time
print("INICIO DEL PROGRAMA")
t1=time.time()
print("TIEMPO T1",t1)
#dormir un tiempo
time.sleep(1)
t2=time.time()
print("TIEMPO T2",t2)
print("FIN DEL PROGRAMA")
print("TIEMPO",t2-t1)
#crear un objeto de la clase VideoCapture
camara1=cv2.VideoCapture(1)
#crear objeto para definir el formato de compresión
formato=cv2.VideoWriter_fourcc(*'MJPG')# ('M','J','P','G')
#crear objeto para definir el nombre del video a crear
video=cv2.VideoWriter("video1.avi",formato,30,(640,480))
#tiempo de referencia
tref1=time.time()
while True:
    #esperar 8 segundos o un teclado 'q'
    if (time.time()-tref1)>=30 or cv2.waitKey(1)==ord("q"):
        #liberar la camara del ordenador
        camara1.release()
        #liberar el video creado
        video.release()
        #destruir todas las ventanas
        cv2.destroyAllWindows()
        break
    ret,frame=camara1.read()
    #mostrar el frame que se esta captando
    cv2.imshow("IMAGEN",frame)
    #registrar cada frame en el video que se esta creando
    video.write(frame)
