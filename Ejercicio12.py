#Ejercicio 12
#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es
#un número divisible por 4, pero no si es divisible por 100, excepto que también sea
#divisible por 400.

anio = int(input("Introduce un año: "))

if anio % 400 == 0:
    print("Es bisiesto")
elif anio % 100 == 0:
    print("No es bisiesto")
elif anio % 4 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")