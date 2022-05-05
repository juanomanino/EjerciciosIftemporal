"""Ejercicio 7:
Programa para calcular e imprimir las raíces de la ecuación de
 segundo grado de coeficientes reales."""


from cmath import sqrt


print("-------------------------------------------")
print("--------RAICES ECUACION SEGUNDO GRADO -----")
print("-------------------------------------------")


# input
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

#processing

d=b**2-4*a*c

if d>0:
    x1=(-b+sqrt(d))/2*a
    x2=(-b-sqrt(d))/2*a
    
    print("El valor de X1 es: "+str(x1)+"y el valor de X2 es: "+str(x2))
else:
    if d==0:
        x1=-b/2*a
        print("El valor de X1 y X2 es: "+str(x1))
    else:
        print("Son raices imaginarias o complejas")

