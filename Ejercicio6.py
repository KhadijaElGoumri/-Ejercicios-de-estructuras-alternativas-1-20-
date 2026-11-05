#Ejercicio 6
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula


letra = input("Introduce una letra: ")

if len(letra) == 1 and letra.isalpha() and letra.isupper():
    print("Es una letra mayúscula")
else:
    print("No es una letra mayúscula")