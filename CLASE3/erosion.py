import cv2
import numpy as np
img=cv2.imread("zard.jpg")
#escala de gris
gris=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
umbral=100
#where del modulo numpy
bin=np.where(gris<=umbral,255,0)
#convertir a entero de 8 bits sin signo
binx=np.uint8(bin)
cv2.imshow("IMAGEN BINARIA X",binx)
kernel=255*np.ones((5,5),dtype=int)
print(kernel)
biny=cv2.erode(binx,kernel=kernel,iterations=1)
cv2.imshow("IMAGEN BINARIA Y (+ EROSIÓN)",biny)
bind=cv2.dilate(biny,kernel=kernel,iterations=1)
cv2.imshow("IMAGEN BINARIA Z (+EROSIÓN+DILATACIÓN)",bind)
cv2.waitKey(0)
cv2.destroyAllWindows()