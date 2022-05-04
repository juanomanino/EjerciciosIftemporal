"""Ejercicio 4:
Programa que le indique el precio de venta de un articulo dado"""


print("-------------------------------")
print("-------PRECIO DE VENTA --------")
print("-------------------------------")


# input
preciocosto=float(input("Digite el precio del artículo: "))


#processing

if preciocosto<3000:
     ganancia=preciocosto*0.15
else:
    if preciocosto<=6000: 
        ganancia=500
    else:
        ganancia=preciocosto*0.25
#output
p=preciocosto+ganancia

print("El precio de venta del artículo de costo " +str(preciocosto)+ " es: "+str(p))