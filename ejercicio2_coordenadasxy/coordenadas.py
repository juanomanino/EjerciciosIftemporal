"""Ejercicio 2:
Programa que lea las coordenadas cartesianas (x, y) de un punto en el plano y calcule el cuadrante 
al cual pertenece el punto. Si el punto está sobre un eje también debe indicarlo."""


print("-------------------------------")
print("------------CUADRANTE PLANO CARTESIANO -------------")
print("-------------------------------")


# input
x=int(input("Digite la coordenada x: "))
y=int(input("Digite la coordenada y: "))


#processing
if x==0 and y==0:
    print("El punto esta sobre el eje x y el eje y")
elif x==0:
    print("El punto esta sobre el eje x")
elif y==0:
    print("El punto esta sobre el eje y")

if x>0 and y>0:
    print("El punto pertenece al cuadrante I")
elif x<0 and y>0:
    print("El punto pertenece al cuadrante II")
elif x<0 and y<0:
    print("El punto pertenece al cuadrante III")
elif x>0 and y<0:
    print("El punto pertenece al cuadrante IV")
