"""
crear arreglo de 2D mediante numpy

"""
import numpy as np
#CREAR ARREGLO DE 2D
a2=np.array( [ [ 1,0,4] , [1,3,10] ] )
#CREAR UNA COPIA DEL ARREGLO a2
b2=a2.copy()
#CREAR UNA VARIABLE c2 =a2+b2
c2=a2-b2
print("LA RESTA DE a2 y b2 ES:")
print(c2)
print("--------------")
#ACCEDER AL ATRIBUTO shape
forma1=a2.shape # (2,3)
#ACCEDER A LA CANTIDAD DE FILAS
Nfil=forma1[0]
#ACCEDER A LA CANTIDAD DE COLUMNAS
Ncol=forma1[1]
#---------------------------------------------------
forma2=b2.shape
print(a2)
print("FORMA DEL ARREGLO A2:",forma1)
print(b2)
print("FORMA DEL ARREGLO B2:",forma2)
