#importar modulos necesarios
import numpy as np
import cv2
import os
#Leer la imagen de entrada en escala BGR
img=cv2.imread("img1.jpg")
#conseguir las filas ,columnas,capas
forma=img.shape
Nf=forma[0]#LARGO ES IGUAL A FILAS
Nc=forma[1]#ANCHO ES IGUAL A COLUMNAS
#realizar una rotación de 45 grados en sentido anti-horario
#(xo,yo)<=> punto centro de la imagen
xo=Nc//2
yo =Nf//2
angulo=30
#CONSEGUIR LA MATRIZ DE ROTACIÓN
R=cv2.getRotationMatrix2D((xo,yo),angulo,1)
#REALIZAR LA ROTACIÓN DE LA IMAGEN DE ENTRADA
imgr=cv2.warpAffine(img,R,(Nc,Nf))
cv2.imshow("IMAGEN 1:",img)
cv2.imshow("IMAGEN ROTADA "+str(angulo),imgr)
#ESPERAR A QUE SE PRESIONE UN BOTON PARA CERRAR LAS IMAGENES
cv2.waitKey(0)
cv2.destroyAllWindows()
#variable que indica el nombre de la carpeta a crear o utilizar
nombre="BASE_DATOS2"
#si en caso la carpeta no esta creada
if (nombre in os.listdir())==False:
    #carpeta con nombre "BASE_DATOS" no existe
    #crear la carpeta
    os.mkdir(nombre)
ruta_referencia=os.getcwd()
print(ruta_referencia)
#ACCEDER A LA CARPETA BASE_DATOS
os.chdir(nombre)
#GUARDAR LA IMAGEN DENTRO DE ESTA CARPETA
cv2.imwrite("img1.png",imgr)
#REGRESAR A LA RUTA DESDE DONDE ENTRE (ruta_referencia)
os.chdir(ruta_referencia)



