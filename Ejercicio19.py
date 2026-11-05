#Ejercicio 19
#Escribe un programa que pida un número entero entre uno y doce e imprima el número
#de días que tiene el mes correspondiente.


mes = int(input("Introduce un mes del 1 al 12: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("Tiene 31 días")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Tiene 30 días")

elif mes == 2:
    print("Tiene 28 días (29 si es bisiesto)")

else:
    print("Error: mes incorrecto")