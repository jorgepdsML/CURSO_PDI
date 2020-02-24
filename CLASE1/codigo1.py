"""
codigo1 en PDI
"""
import numpy as np
import cv2
img=cv2.imread("imagen.png")
img=cv2.resize(img,(150,150))
#BGR A RGB
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
#DETERMINAR CONTENIDO EN COLOR R , G Y B
r=img[:,:,0]
h=hsv[:,:,0]
g=img[:,:,1]
s=hsv[:,:,1]
b=img[:,:,2]
v=hsv[:,:,2]
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
rx=r.flatten()
gx=g.flatten()
bx=b.flatten()
fig=plt.figure()
#ax=fig.add_subplot(111,projection="3d")
ax=Axes3D(fig)
ax.scatter(gx,rx,bx,cmap="rgb")
ax.set_xlabel("CANAL VERDE (G)")
ax.set_ylabel("CANAL ROJO (R)")
ax.set_zlabel("CANAL AZUL (B)")
plt.show()

fig=plt.figure()
#ax=fig.add_subplot(111,projection="3d")
ax=Axes3D(fig)
ax.scatter(s.flatten(),h.flatten(),v.flatten())
ax.set_xlabel("CANAL SATURATION (S)")
ax.set_ylabel("CANAL HUE (H)")
ax.set_zlabel("CANAL VALUE (V)")
plt.show()
import time
time.sleep(1)
plt.close()