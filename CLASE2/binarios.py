#IMAGEN BINARIA
import numpy as np
import cv2
#Leer la imagen de entrada BGR
img=cv2.imread("img1.jpg")
#conversión a escala de grises  GRAY
gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ECUALIZAR EL HISTOGRAMA DE LA IMAGEN DE ENTRADA EN ESCALA DE GRIS
gris2=cv2.equalizeHist(gris)
#binarización por umbral
umbral=120
#utilizar función where del paquete numpy
bina=np.where(gris<=umbral,255,0) #flotante
bina2=np.where(gris2<=umbral,255,0)#flotante
#convertir a entero
bina=np.uint8(bina)
#imagen binaria 2 a entero
bina2=np.uint8(bina2)
#OPERACIÓN LOGICA AND
#----BGR--- INPUT
img4=cv2.bitwise_and(img,img,mask=bina2)
#---BGR ---- OUTPUT
cv2.imshow("IMAGEN GRIS",gris)
cv2.imshow("IMAGEN BGR",img)
cv2.imshow("IMAGEN BINARIA2",bina2)
cv2.imshow("IMAGEN DESPUES DE LA OPERACIÓN AND",img4)
#mostra la relación de pixeles blanco con respecto al total de pixeles
forma=img.shape
nf=forma[0] #número de filas  de la imagen
nc=forma[1] #número de columnas de la imagen
cont=0 #definir el area
#acceder a las filas
for f in range(nf):
    for c in range(nc):
        if bina2[f,c]==255:
            cont=cont+1
Ratio=np.round(100*cont/(nf*nc))
print("EL RATIO ES:",Ratio)
cv2.waitKey(0)
cv2.destroyAllWindows()


