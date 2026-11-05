#Ejercicio 10
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
#circunferencias y las clasifique en uno de estos estados:
#• exteriores
#• tangentes exteriores
#• secantes
#• tangentes interiores
#• interiores
#• concéntricas

import math

x1 = float(input("Introduce x1: "))
y1 = float(input("Introduce y1: "))
x2 = float(input("Introduce x2: "))
y2 = float(input("Introduce y2: "))

r1 = float(input("Introduce el radio 1: "))
r2 = float(input("Introduce el radio 2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if r1 <= 0 or r2 <= 0:
    print("Radios incorrectos")

elif distancia == 0:
    print("Concéntricas")

elif distancia > r1 + r2:
    print("Exteriores")

elif distancia == r1 + r2:
    print("Tangentes exteriores")

elif distancia > abs(r1 - r2):
    print("Secantes")

elif distancia == abs(r1 - r2):
    print("Tangentes interiores")

else:
    print("Interiores")
