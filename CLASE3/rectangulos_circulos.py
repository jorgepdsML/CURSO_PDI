import cv2
img=cv2.imread("imagen1.jpg")
#conseguir filas(alto) , columnas(ancho) y canales
forma=img.shape
alto=forma[0]
ancho=forma[1]
canales=forma[2]
xo=alto//2
yo=alto//2
ro1,ro2=20,170
cv2.circle(img,(xo,yo),ro1,(0,255,255),2)
cv2.circle(img,(xo,yo),ro2,(255,0,0),2)
cv2.imshow("IMAGEN",img)
cv2.waitKey(0)



cv2.destroyAllWindows()