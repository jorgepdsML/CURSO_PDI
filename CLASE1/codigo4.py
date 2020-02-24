import cv2
img=cv2.imread("imagen.png")
xo=20
yo=50
x1=300
y1=200
cv2.rectangle(img,(yo,xo),(y1,x1),(0,255,0),3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Texto',(yo,xo), font, 1,(0,255,255),2,cv2.LINE_AA)
cv2.imshow("IMAGEN CON UN RECTANGULO",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""import cv2
from matplotlib import pyplot as plt
img=cv2.imread("imagen.png")
#escala de grises
gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Histograma
histo1=cv2.calcHist([gris],[0],None,[256],[0,256])
#ECUALIZACIÓN DE HISTOGRAMA
gris2=cv2.equalizeHist(gris)
#Histograma 2
histo2=cv2.calcHist([gris2],[0],None,[256],[0,256])
plt.subplot(121)
plt.plot(histo1)
plt.title("HISTOGRAMA")
plt.ylabel("N° DE PIXELES")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.subplot(122)
plt.plot(histo2)
plt.title("HISTOGRAMA ECUALIZADO")
plt.ylabel("N° DE PIXELES")
plt.xlabel("NIVEL DE INTENSIDAD")
plt.show()
cv2.imshow("IMAGEN GRAY",gris)
cv2.imshow("IMAGEN GRAY ECUALIZADA",gris2)
cv2.waitKey(0)
borde1=cv2.Canny(gris,20,195)
borde2=cv2.Canny(gris2,20,195)
cv2.imshow("BORDE GRAY",borde1)
cv2.imshow("BORDE GRAY ECUALIZADA",borde2)
cv2.waitKey(0)"""