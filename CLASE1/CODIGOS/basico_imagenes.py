"""
ARREGLO DE 3 DIMENSIONES
"""
#---IMPORTAR HERRAMIENTAS NECESARIAS
import numpy as np
import cv2
#de matplotlib vamos a import solo el modulo pyplot
from matplotlib import pyplot as plt

#------------------------------------------------------------
#función imread() pertenece a la liberia opencv(cv2)
#Especificar ruta o solo el nombre(cuando se encuentra en la misma carpeta del archivo de python)
# -------------B-G-R------------------------
img=cv2.imread("imagen5.png")
#----------R-G-B-------------------
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#CONVERTIR DE LA ESCALA BGR HACIA LA ESCALA GRAY
gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ECUALIZAR EL HISTOGRAMA DE LA IMAGEN EN ESCALA DE GRIS
gris_equ=cv2.equalizeHist(gris)
#REALIZAR EL CALCULO DEL HISTOGRAMA
histo=cv2.calcHist([gris],[0],None,[256],[0,256])
#REALIZAR LA SIGUIENTE OPERACIÓN , RESULTADO EN FLOTANTE , DECIMALES
c=1.5
b=50
#realizar una copia de la matriz
I2=gris.copy()
#REALIZAR UN RECORRIDO SOBRE LAS FILAS Y COLUMNAS
#---------------------------------------------------------------------------------
forma=I2.shape
Nf=forma[0]
Nc=forma[1]
#recorrido sobre las filas
for x in range(Nf):
    #recorrido sobre las columnas
    for y in range(Nc):
        #saturación maxima
        if (c*gris[x,y]+b)>=255:
            I2[x,y]=255
        #saturación minima
        elif (c*gris[x,y]+b)<=0:
            I2[x,y]=0
        #dentro del intervalo
        else:
            I2[x,y]=c*gris[x,y]+b
         
#---------------------------------------------------------------------------------
#CONVERTIR DE FLOTANTE A ENTERO DE 8 BITS SIN SIGNO()
I2=np.uint8(I2)
#HISTOGRAMA 2
histo2=cv2.calcHist([gris_equ],[0],None,[256],[0,256])
cv2.imshow("IMAGEN GRIS MODIFICADA",gris_equ)
#-------------------------------------------------
#COPIAR IMAGEN ORIGINAL Y ASIGNARLE A LA VARIABLE img2
img2=img.copy()
#ACCEDER A LA CAPA ROJA
img2[ :,: ,2]=0
print("EL TIPO DE DATO ES;",img.dtype)
#uso de atributo shape
forma=img.shape
#CREAR VARIABLE PARA ALMACENAR FILAS , COLUMNAS Y CANALES
nfils,ncols,canales=forma[0],forma[1],forma[2]
print("LA FORMA ES:",forma)
print("FILAS:",nfils,"COLUMNAS:",ncols,"CANALES:",canales)
print("FORMA DE LA IMAGEN ESCALA DE GRISES ",gris.shape)
#MOSTRAR LA IMAGEN
#---------B-G-R
cv2.imshow(" IMAGEN ORIGINAL",img)
cv2.imshow("IMAGEN SIN ROJO",img2)
#MOSTRAR IMAGEN EN ESCALA DE GRISES
cv2.imshow("IMAGEN EN ESCALA GRAY",gris)
#ESPERAR UN TECLA PARA FINALIZAR EL PROGRAMA
cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.subplot(121)
plt.plot(histo)
plt.title("HISTOGRAMA ")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NÚMERO DE PIXELS")
plt.subplot(122)
plt.plot(histo2)
plt.title("HISTOGRAMA ")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.ylabel("NÚMERO DE PIXELS")
plt.show()
cv2.destroyAllWindows()
print("FIN DEL CODIGO")
