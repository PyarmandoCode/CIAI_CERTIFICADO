"""
Funciones
"""

def total_producto(pre,cant,nom=None):
    total=pre*cant
    msj=f"El Total a pagar por el producto {nom} es {total}"
    return msj

print(total_producto(1200,23,"Laptop"))


"""
Librerias 
Son del Nucleo de python
"""
import math 
print(math.pi)
print(math.sqrt(4))
print(math.cos(5))

import statistics
datos=[2.90,10.5,14.7,23.7,10.5]
print(statistics.variance(datos)) # la varian
print(statistics.mode(datos)) #la moda
print(statistics.mean(datos)) #el promedio

from datetime import datetime
print(datetime.now())



