#IMPORTAR NUMPY COMO np
import numpy as np
#CREAR UN ARREGLO UTILIZANDO NUMPY
#ESCALAR
a0=np.array(10.5)
#ARREGLO DE 1D
a1=np.array([30,20,100])
print("ARREGLO A1:",a1)
print("FORMA DEL ARREGLO a1: ",a1.shape)
#REALIZAR LA SUMA DE CADA ELEMENTO
#ACCEDER A CADA VALOR
v1=a1[0]
v2=a1[1]
v3=a1[2]
#VARIABLE suma
suma=v1+v2+v3
#MOSTRAR MENSAJE DE VALOR
print("LA SUMA ES:",suma)
