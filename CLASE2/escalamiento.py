#importar herramientas necesarias
import numpy as np
import cv2
#leer la imagen en escala BGR
img=cv2.imread("img1.jpg")
#utilizar el atributo shape
forma=img.shape
#Determinar número de filas
Nf=forma[0]
#Determinar número de columnas
Nc=forma[1]
print("DIMENSIONES DE LA IMAGEN DE ENTRADA",forma)
#-----------PASAR PARAMETROS DE NUEVAS FILAS Y COLUMNAS DESDE LA SHELL DE PYTHON
New_filas=int(input("INGRESAR NUEVAS FILAS"))
New_columnas=int(input("INGRESAR NUEVAS COLUMNAS"))
#--SI EN CASO LA DIMENSIÓN DEL AREA ES MAYOR QUE LA ENTRADA
if New_columnas*New_filas>Nf*Nc:
    img2=cv2.resize(img,(New_columnas,New_filas),interpolation=cv2.INTER_CUBIC)
    print("INTERPOLACIÓN INTER_CUBIC")
#--CUANDO LA DIMENSIÓN DEL AREA ES MENOR QUE LA ENTRADA
elif New_columnas*New_filas<Nf*Nc:
    img2=cv2.resize(img,(New_columnas,New_filas),interpolation=cv2.INTER_AREA)
    print("INTERPOLACIÓN INTER_AREA")
#utilizar el atributo shape
forma2=img2.shape
print("DIMENSIONES DE LA NUEVA IMAGEN",forma2)
cv2.imshow("IMAGEN 1:",img)
cv2.imshow("IMAGEN 2:",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

