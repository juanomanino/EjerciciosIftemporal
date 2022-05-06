"""Ejercicio 10:
Programa que por cada número ingresado del 1 al 7 diga que dia de la semana es en ese orden"""


print("------------------------------------")
print("---------DIAS DE LA SEMANA----------")
print("------------------------------------")


# input
opcion=int(input("Digite un número del 1 al 7: "))


#processing
if opcion==1:
  print("Es Lunes")
elif opcion==2:
  print("Es Martes")
elif opcion==3:
  print("Es Miércoles")
elif opcion==4:
  print("Es Jueves")
elif opcion==5:
  print("Es Viernes")
elif opcion==6:
  print("Es Sábado")
elif opcion==7:
  print("Es Domingo")
else:
  print("Día no válido")

    
