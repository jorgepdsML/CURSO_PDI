import numpy as np
import cv2
#LEER LA IMAGEN EN EL ORDEN B-G-R
img=cv2.imread("imagen5.png")
#MOSTRAR LA FORMA DE LA IMAGEN , FILAS COLUMNAS Y CAPAS
print(img.shape)
#CREAR NUEVA IMAGEN CON DIMENSIÓN 500 x 500
#INTER_CUBIC PARA AUMENTAR LAS DIMENSIONES
img2=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)
#convertir de la escala de BGR HACIA GRIS
gris=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#INCREMENTAR EL BRILLO DE UNA IMAGEN
gris2=cv2.equalizeHist(gris)
kernel=np.array([[-1,0,1],[0,0,0],[-1,0,1]])
#filter2D
filt=cv2.filter2D(gris2,-1,kernel=kernel)
#Canny
bordes1=cv2.Canny(gris,10,200)
bordes2=cv2.Canny(gris2,10,200)

cv2.imshow("GRISES",gris)
cv2.imshow("GRISES 2",gris2)
cv2.imshow("IMAGEN BORDES 1 DE LA IMAGEN SIN ECUALIZAR",bordes1)
cv2.imshow("IMAGEN BORDES 2 DE LA IMAGEN ECUALIAZADA",bordes2)

#DETERMINAR EL HISTOGRAMA DE UNA IMAGEN EN ESCALA DE GRISES
#PIXEL TIENE COMO MAXIMO 256 NIVELES DE INTENSIDAD (8 BITS SIN SIGNO)
histo=cv2.calcHist([gris],[0],None,[256],[0,256])
histo2=cv2.calcHist([gris2],[0],None,[256],[0,256])

from matplotlib import pyplot as plt
plt.subplot(121)
plt.plot(histo)
plt.xlabel("INTENSIDAD")
plt.ylabel("NUMERO DE PIXELES")
plt.subplot(122)
plt.plot(histo2)
plt.xlabel("INTENSIDAD")
plt.ylabel("NUMERO DE PIXELES")

plt.show()
#INTER_AREA PARA REDUCIR LAS DIMENSIONES
img3=cv2.resize(img,(150,200),interpolation=cv2.INTER_AREA)
#MOSTRAR LA IMAGEN EL ORDEN B G R
cv2.imshow("MI IMAGEN",img)
cv2.imshow("MI IMAGEN 500x500",img2)
cv2.imshow("MI IMAGEN 200x150",img3)
#ESPERAR A PRESIONAR A UNA TECLA
cv2.waitKey(0)
print("FIN DEL CODIGO")