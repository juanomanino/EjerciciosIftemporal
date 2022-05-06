"""Ejercicio 9:
Programa que lea dos números enteros y averigüe si el uno es múltiplo del otro"""


print("-------------------------------")
print("------------MULTIPLOS----------")
print("-------------------------------")


# input
a=int(input("Ingrese el valor del primer entero: "))
b=int(input("Ingrese el valor del segundo entero: "))


#processing
if a>b:
    x=a/b
    if (int(x)==x):
      print("El numero "+str(a)+" es múltiplo del número "+str(b))
    else:
      print("El numero "+str(a)+" NO es múltiplo del número "+str(b))
else:
    x=b/a
    if (int(x)==x):
        print("El numero "+str(b)+" es múltiplo del número "+str(a))
    else:
     print("El numero "+str(b)+" NO es múltiplo del número "+str(a))

