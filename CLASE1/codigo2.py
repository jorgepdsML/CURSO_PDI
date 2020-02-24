import numpy as np
import cv2
img=cv2.imread("imagen.png")
#rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h=hsv[:,:,0]
hsv[:,:,0]=hsv[:,:,2]
hsv[:,:,2]=h
#CONCETRACIÓN DE COLOR ROJO
condicion=(img[:,:,2]>10) & (img[:,:,2]<200)
print(type(condicion))
ct=np.where( condicion,1,0)
#contar cuantos superaron el umbral
nz=np.count_nonzero(ct)
ct=nz/np.size(img)
cv2.imshow("RGB",img)
print("CONCENTRAACIÓN DE ROJO",ct)
cv2.imshow("HSV",hsv)
cv2.waitKey(0)