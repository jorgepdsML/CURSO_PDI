#importar los modulos necesarios
import numpy as np
import cv2
#-uso de filtrado gaussiano , binarización por umbral
#crear un objeto que permite poder leer las imagenes de nuestra camara
camara=cv2.VideoCapture(0)
min_azul=np.array([100,65,65])
max_azul=np.array([120,255,255])
while True:
    #leer las imagenes o frames de la camara(BGR)
    estado,frame=camara.read()
    #cambiar escala BGR a HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #---binarizar la imagen hsv con la función inRange---
    mascara_azul=cv2.inRange(hsv,min_azul,max_azul)
    #operación de erosión
    kernel1=255*np.ones((5,5),dtype=int)
    #erosioón de la imagen binaria de entrada (mascara_azul)
    mascara_azul_erosion=cv2.erode(mascara_azul,kernel=kernel1,iterations=2)
    mascara_azul_dilatada=cv2.dilate(mascara_azul_erosion,kernel=kernel1,iterations=1)
    #operación and entre la mascara y la imagen BGR
    solo_azul=cv2.bitwise_and(frame,frame,mask=mascara_azul_dilatada)
    cv2.imshow("MASCARA DE REGION AZUL",mascara_azul)
    cv2.imshow("MASCARA DE REGION AZUL + EROSIÓN",mascara_azul_dilatada)
    cv2.imshow("IMAGEN CON CONTENIDO AZUL",solo_azul)
    #convertir a escala de gris
    gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #ecualizar el histograma (realzar el contraste de la imagen gris)
    gris2=cv2.equalizeHist(gris)
    #uso de la función where
    #----------------------------------
    umbral=100
    mascara1=np.where(gris2<=umbral,255,0)
    mascara1=np.uint8(mascara1)
    #-----------------------------------
    #--------Binarización basado en el color

    #-----------------------------------------
    #mostar los frames
    cv2.imshow("FRAME CAPTURADO EN BGR",frame)
    #cv2.imshow("IMAGEN BINARIA",mascara1)
    if cv2.waitKey(1)==ord("q"):
        break
#Liberar el uso de la camara del ordenador, método release()
camara.release()
#luego de liberar , cerrar las ventanas
cv2.destroyAllWindows()