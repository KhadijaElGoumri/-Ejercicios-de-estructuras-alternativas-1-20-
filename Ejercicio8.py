#Ejercicio 8
#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje
#‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y
#el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir
#‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

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

