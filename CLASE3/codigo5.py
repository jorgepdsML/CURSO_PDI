#slicing de arrays
import cv2
img=cv2.imread("zard.jpg")
xo=140
yo=50
w=120
h=100
#realizar una copia de la imagen
imgref=img.copy()
#recorte de la imagen
img2=img[yo:yo+h,xo:xo+w,:]
#mostrar imagen original
cv2.rectangle(imgref,(xo,yo),(xo+w,yo+h),(255,0,0),2)
cv2.imshow("IMAGEN1",imgref)
#mostrar imagen recortada
cv2.imshow("IMAGEN2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("img2.jpg",img2)
