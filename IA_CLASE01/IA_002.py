"""
PROCESOS SECUENCIALES
-CONDICIONALES
-BUCLES
"""
#condicionales
# precio = float(input("Ingrese el precio del producto:"))
# if precio >= 100 and precio<=199:#identacion
#     print("El producto esta en el rango 1") #VERDADERO
# elif precio >=200 and precio<=299:
#     print("El precio esta en el rango 2")    
# elif precio >=300 and precio<=399:
#     print("El precio esta en el rango 3")        
# else:
#     print("El precio es menor que los rangos ") #FALSO    

#bucles
#for - while
# valores = list() #constructor inicializar la lista
# for i in range(1,10,2):
#     if i==5 or i==6:
#         continue #salta los valores indicados
#     if i==8:
#         break #sale del bucle
#     else:
#         valores.append(i)#añadir elementos a la lista
#         print(f"{valores} CIAI")

valores = list() 
num=0
while num<10:#True
    num=num+1
    if num==5 or num==6:
        continue #salta los valores indicados
    if num==8:
        break #sale del bucle
    else:
        valores.append(num)#añadir elementos a la lista
        print(valores)