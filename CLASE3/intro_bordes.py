import numpy as np
import cv2
cap=cv2.VideoCapture(1)
#definir kernels
#kernel 1
Hx=np.array([[-1,0,1],
             [-1,0,1],
             [-1,0,1]])
Hy=np.array([[-1,-1,-1],
             [0,0,0],
             [1,1,1]])
while True:
    ret,frame=cap.read()
    #convertir a gris
    gris=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #filtrado gaussiano
    gris=cv2.GaussianBlur(gris,(3,3),1)
    #ecualizar el histograma
    gris=cv2.equalizeHist(gris)
    #realizar la operación de convolución 2d
    outputx=cv2.filter2D(gris,-1,kernel=Hx)
    outputx=outputx.astype(np.float)
    outputy=cv2.filter2D(gris,-1,kernel=Hy)
    outputy=outputy.astype(np.float)

    outputxy=np.sqrt(outputx**2+outputy**2)
    #realizar una binarización
    binx=np.where(outputx>=25,255,0)
    biny=np.where(outputy>=25,255,0)
    binxy=np.where(outputxy>=25,255,0)
    binx=np.uint8(binx)
    biny=np.uint8(biny)
    binxy=np.uint8(binxy)
    cv2.imshow("IMAGEN ORIGINAL",frame)
    cv2.imshow("IMAGEN BINARIA XY",binxy)
    if cv2.waitKey(1)==ord("s"):
        cap.release()
        cv2.destroyAllWindows()

