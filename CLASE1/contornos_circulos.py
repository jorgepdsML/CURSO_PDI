import numpy as np
import cv2
#crear objeto
video=cv2.VideoCapture(0)
while True:
    #leyendo las imagenes
    estado,img=video.read()
    #CONVERTIR A ESCALA DE GRISES
    gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #REALIZAR UNA ECUALIZACIÓN
    gris=cv2.equalizeHist(gris)
    #UTILIZAR EL FILTRO DE CANNY PARA DETECTAR LOS BORDES
    #bordes=cv2.Canny(gris,20,200)
    #REALIZAR UNA BUSQUEDA DE OBJETO CIRCULARES
    #IMAGEN EN GRISES,RESOLUCION DE 1 PIXEL , MINIMA DISTANCIA ENTRE CIRCULOS 40
    #param1=40 , param2=60 , minRadius= radio minimo de busqueda , maxRadius
    circulos=cv2.HoughCircles(gris,cv2.HOUGH_GRADIENT,1,50,param1=40,param2=60,minRadius=35,
                              maxRadius=120)
    #utilizar un bucle for para graficar los objetos circulares
    #determinar si hay circulos
    if circulos is not None and circulos.shape[1]<=5:
        for c in circulos[0,:]:
            #cv2.circle(imagen,(xo,yo),ro,(b,g,r),grosor)
            cv2.circle(img, (c[0],c[1]), c[2], (0, 255, 255), 3)
    cv2.imshow("IMAGEN CAPTURA ES:",img)
    if cv2.waitKey(1)==ord("s"):
        video.release()
        cv2.destroyAllWindows()
        break
    #xo,yo y el radio ro
    #DIBUJAR LOS OBJETOS CIRCULARES DETECTADOS