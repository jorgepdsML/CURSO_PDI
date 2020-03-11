import cv2
#crear objeto de la clase VideoCapture()
camara1=cv2.VideoCapture(0)
#crear objeto de la clase VideoWriter()
formato=cv2.VideoWriter_fourcc(*'MJPG')# ('M','J','P','G')
video=cv2.VideoWriter("video1.avi",formato,20,(640,480))
#camara2=cv2.VideoCapture(1)
print(type(camara1))
#objeto.método
#isOpened()
print(camara1.isOpened())
#tomar una foto luego de presionar una tecla
input("PRESIONAR UN BOTON PARA CONTINUAR")
#leer un frame
ret,frame=camara1.read()
#ret2,frame2=camara2.read()
cv2.imshow("IMAGEN1",frame)
#cv2.imshow("IMAGEN2",frame2)
#esperar hasta que se presione un teclado para almacenar el archivo
cv2.waitKey(0)
#guardar el frame con un nombre en extensión jpg
cv2.imwrite("imagen1.jpg",frame)
#cv2.imwrite("imagen2.jpg",frame2)
#liberar la camara
camara1.release()
cv2.destroyAllWindows()