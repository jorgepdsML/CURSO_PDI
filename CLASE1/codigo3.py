import numpy as np
import cv2
img=cv2.imread("imagen.png")
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
camara=cv2.VideoCapture(0)
cont=0
while True:
    #lectura de camara  (BGR)
    ret,frame1=camara.read()
    frame1=cv2.resize(frame1,(800,600))
    #realizar la busqueda de circulos
    gray=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    #IMAGEN EN ESCALA RGB
    frame=cv2.cvtColor(frame1,cv2.COLOR_BGR2RGB)
    #---FILTRADO GAUSSIANO
    gray=cv2.GaussianBlur(gray,(3,3),1)
    #ECUALIZACIÓN
    gray=cv2.equalizeHist(gray)
    Nf,Nc=gray.shape
    #busqueda de circulos
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50 ,
                               param1=65, param2=60, minRadius=50, maxRadius=150)
    cv2.imshow("IMAGEN", frame1)
    if cv2.waitKey(1)==ord("f"):
        break
    if circles is not None and circles.shape[1]==1:
        for i in circles[0, :]:
            i2=i.copy()
            #print("hay circulos")
            #---MEDIDAS DEL CENTRO FILA X0 , COLUMNA Y0 , RADIO r
            xo,yo,ro=int(i2[1]),int(i2[2]),int(i2[2])
            r=ro-1
            #determinar el contenido en color
            #realizar el recoriddo siempre y cuando el objeto
            #este dentro de la imagen
            if 1.4*ro<Nf and 1.4*ro<Nc and xo>r and yo>r and xo+r<Nf and yo+r<Nc :
                # DETERMINAR EL AREA
                area = int(3 * ((r) ** 2))
                # draw the outer circle
                cv2.circle(frame1, (i[0], i[1]), i[2], (10,50, 170), 5)
                # draw the center of the circle
                cv2.circle(frame1, (i[0], i[1]), 2, (0, 0, 255), 3)
                cv2.imshow("IMAGEN", frame1)
                if cv2.waitKey(1) == ord("f"):
                    break
                #--RECORRIDO SOBRE EL SEGUNDO CUADRANTE
                dec=0
                import time
                for x in range(xo-r,xo+1,1):
                    #dec = dec + 1
                    #print("EJE Y N°",x)
                    for y in range(-r+dec,yo+1,1):
                     #   print("EJE X N° ",y)
                    #    time.sleep(0.1)
                        if dec>= r:
                            break
                        #DETERMINAR CUANTOS PIXELES SUPERARN EL UMBRAL
                        if frame[x,y+yo,2]>=2:
                            cont = cont + 1
                    dec = dec + 1
                if cont>0:
                    ct=100*(4*cont/area)
                    cont = 0
                    if ct>=5:
                        print("CONCENTRACIÓN DE AZUL ES : ", ct)
                cont=0

cv2.destroyAllWindows()
camara.release()
if isinstance(circles,np.ndarray):
    print(circles, type(circles),np.shape(circles))
    print(np.shape(frame))
    #print(np.shape(circles[0,:]))