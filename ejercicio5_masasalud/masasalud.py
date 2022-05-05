"""Ejercicio 5:
Programa que calcule el índice de masa corporal de una persona indique el estado en el que se encuentra esa persona en función del valor del IMC:"""


print("-------------------------------")
print("----INDICE MASA CORPORAL -------")
print("-------------------------------")


# input
peso=int(input("Ingrese su peso: "))
alt=float(input("Ingrese su altura: "))

#processing
imc=peso/(alt**2)
if imc<=16:
     print("¡Usted se encuentra en un criterio de ingreso en hospital!")
else:
    if imc<=17: 
        print("Usted tiene infrapeso")
    else:
        if imc<=18: 
            print("Usted tiene un peso bajo")
        else:
            if imc<=25: 
                print("Usted tiene un peso normal. Está saludable")
            else:
                if imc<=30: 
                    print("Usted tiene sobrepeso (obesidad de grado I)")
                else:
                    if imc<=35: 
                        print("Usted tiene sobrepeso crónico (obesidad de grado II)")
                    else:
                        if imc<=40: 
                             print("Usted tiene obesidad premórbida(obesidad de grado III)")
                        else:
                            if imc>40: 
                                 print("Usted tiene obesidad mórbida (obesidad de grado IV)")