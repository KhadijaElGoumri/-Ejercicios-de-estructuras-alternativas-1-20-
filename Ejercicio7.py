#Ejercicio 7
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
#exponente. Pueden ocurrir tres cosas:
#• El exponente sea positivo, sólo tienes que imprimir la potencia.
#• El exponente sea 0, el resultado es 1.
#• El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.


base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
    print("Resultado:", resultado)

elif exponente == 0:
    print("Resultado: 1")

else:
    if base != 0:
        resultado = 1 / (base ** abs(exponente))
        print("Resultado:", resultado)
    else:
        print("Error: no se puede dividir entre cero")