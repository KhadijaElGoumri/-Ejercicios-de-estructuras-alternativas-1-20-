
#Ejercicio 9
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);


a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
c = float(input("Introduce el tercer número: "))

if a >= b and a >= c:
    mayor = a
    if b >= c:
        medio = b
        menor = c
    else:
        medio = c
        menor = b

elif b >= a and b >= c:
    mayor = b
    if a >= c:
        medio = a
        menor = c
    else:
        medio = c
        menor = a

else:
    mayor = c
    if a >= b:
        medio = a
        menor = b
    else:
        medio = b
        menor = a

print("Orden:", mayor, medio, menor)