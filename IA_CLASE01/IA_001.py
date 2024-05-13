"""
Comentario en Varias Lineas
"""
#comentario en una linea
print("Bienvenido al curso de IA")#esto es otro comentario
 
"""
Variables
Tipos de datos Primitivos
"""
#Tipo String
nombre = "Armando"
apellido = 'Ruiz' 
#Tipo Numericos
edad= 48 #int
sueldo= 1200.89 #float
#Tipo Bool
estado=True
#Estructura de datos
valores = [12,18,14,29,34,120] #listas
productos = {
    "A100":"XYZ",
    "A200":"XYL",
    "A300":"XYM",
    "A400":"XY0"
  } #diccionarios
# print(productos.keys())
# print(productos.values())
# print(productos["A200"]) #XYL
#tuplas inmutables
precios=(1200,1788,2000)
#conjuntos (sets)
cantidades = {12,45,67,89,12,12,89,23}#no ordenados,sin duplicados
"""
Entrada de datos
"""
precio = float(input("Precio del Producto:"))
total = precio / 12 #si deseas capturar con n decimales usa //
print(f"El Total hallado es {round(total,2)}")


