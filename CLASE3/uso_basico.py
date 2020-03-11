import cv2
#objeto para manipular camara de ordenador
cap2=cv2.VideoCapture(1)
#determinar si esta activo , método isOpened()
print("activado camara externa:",cap2.isOpened())
#determinar el FRAME RATE de la camara
fps=cap2.get(cv2.CAP_PROP_FPS)
print(fps)
#liberar la camara
cap2.release()
