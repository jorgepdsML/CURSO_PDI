"""
Crear objeto para la manipulación de la camara
"""
import numpy as np
import cv2
#-------------
video=cv2.VideoCapture(0)
#ingresar a un bucle while
blue_min=np.array([80,110,110])
blue_max=np.array([120,255,255])
while True:
    #CAPTAR IMAGEN DE LA CAMARA
    estado,img=video.read()
    img=cv2.resize(img,(400,400),interpolation=cv2.INTER_AREA)
    #ATENUAR EL RUIDO
    img=cv2.GaussianBlur(img,(5,5),1)
    #convertir de la escala BGR A HSV
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #REALIZAR LA SEGMENTACIÓN
    azul=cv2.inRange(hsv,blue_min,blue_max)
    #REALIZAR OPERACIÓN MORFOLOGICA
    filtro=np.ones((7,7),dtype=np.float32)
    #EROCIÓN (ELIMINAR PIXELES DE LA ULTIMA CAPA)
    morfo=cv2.erode(azul,filtro,iterations=4)
    #DILATACIÓN (AÑADIR PIXELES EN LA ULTIMA CAPA)
    morfo=cv2.dilate(morfo,filtro,iterations=4)
    #resultado1
    resultado1=cv2.bitwise_and(img,img,mask=azul)
    #resultado2
    resultado2=cv2.bitwise_and(img,img,mask=morfo)
    #DETERMINAR EL CONTORNO DE LA IMAGEN BINARIA morfo
    contorno,jerarquia=cv2.findContours(morfo,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #GRAFICAR TODOS LOS CONTORNOS
    for c in contorno:
        # (B,G,R)
        cv2.drawContours(resultado2,[c],0,(0,255,255),1)
    #H(0-179) HUE , S SATURATION(0-255)  , V VALUE(0-255)
    #cv2.imshow("LA IMAGEN ES:",img)
    #cv2.imshow("IMAGEN RESULTADO,SIN FILTRO MORFOLOGICO", resultado1)
    cv2.imshow("IMAGEN RESULTADO,CON FILTRO MORFOLOGICO",resultado2)
    #cv2.imshow("IMAGE BINARIA AZUL,CON FILTRO MORFOLOGICO",morfo)
    #cv2.imshow("IMAGEN BINARIA AZUL,SIN FILTRO MORFOLOGICO",azul)
    if cv2.waitKey(1)==ord("q"):
        break
video.release()
cv2.destroyAllWindows()