"""Ejercicio 6:
Programa para calcular el gasto de agua de una vivienda dado el número de m2 de agua gastados"""

print("--------------------------------------")
print("-------PRECIO AGUA POR M2-------------")
print("--------------------------------------")


# input
agua=int(input("Ingrese los m² que gasto este mes: "))

#processing

if agua<=50:
    gasto=10000
    print("Su gasto de agua equivale a $"+str(gasto))
else:
    if agua<=200:
        gasto=((agua-50)*2000)+10000
        print("Su gasto de agua equivale a $"+str(gasto))
    else:
        gasto=((agua-50)*3000)+10000
        print("Su gasto de agua equivale a $"+str(gasto))
