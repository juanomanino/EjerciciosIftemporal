"""Ejercicio 3:
Programa para verificar si una persona es apta para un préstamo
bancario"""


print("-------------------------------")
print("---------PRESTAMO -------------")
print("-------------------------------")


# input
ingr=int(input("Digite sus ingresos: "))
#processing

if ingr>945200:
    deuda=int(input("¿Tiene alguna otra deuda? Digite 1 para si, Digite 2 para no: "))
    if deuda==2:
        print("Usted es apto para el préstamo. Aprobado")
    else:
        print("Prestamo denegado")
else:
    print("Prestamo denegado")
