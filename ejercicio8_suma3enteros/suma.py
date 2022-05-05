"""Ejercicio 8:
para determinar si dados tres números enteros, la suma de los dos primeros es igual al tercero"""


print("-------------------------------")
print("-------SUMA DOS ENTEROS -------")
print("-------------------------------")


# input
x=int(input("Ingrese el valor del primer entero: "))
y=int(input("Ingrese el valor del segundo entero: "))
c=int(input("Ingrese el valor del tercer entero: "))


#processing

z=x+y
if z==c:
    print("La suma de los dos primeros enteros es igual al tercero")
else:
    print("La suma de los dos primeros no es igual al tercer entero")
