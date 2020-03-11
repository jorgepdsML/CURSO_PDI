import cv2
import numpy as np
i=np.array([[0,0,0,0],[0,255,255,0],[0,255,0,0],[0,0,0,0]])
i=np.uint8(i)
k=np.array([[0,0,0],[0,255,255],[0,255,0]])
k=np.uint8(k)
i2=cv2.erode(i,kernel=k)
print(i2)
l=[10,20,30]
