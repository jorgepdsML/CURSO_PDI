"""
uso de opencv para dibujar rectangulos
"""
import numpy as np
import cv2
img=cv2.imread("zard.jpg")
#dibujar un rectangulo
#determinar filas (alto), columnas(ancho),canales(capas)
forma=img.shape #(Nf,Nc,canales)
alto=forma[0]
ancho=forma[1]
#elegir 2 puntos de coordenadas
xo=10
yo=20
x1=120
y1=140
#rectangle devuelve la imagen con el rectangulo superpuesto
img2=cv2.rectangle(img,(xo,yo),(x1,y1),(255,0,0),2)
#mostrar la imagen utilizando imshow
cv2.imshow("IMAGEN",img)
#esperar una tecla para salir del programa
cv2.waitKey(0)
#almacenar la imagen con el rectangulo sobre la imagen
cv2.imwrite("imagenrect.jpg",img2)
#cerrar todas las ventanas abiertas
cv2.destroyAllWindows()

