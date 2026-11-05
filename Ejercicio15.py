#Ejercicio 15
#El director de una escuela está organizando un viaje de estudios, y requiere determinar
#cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
#servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
#alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95
#euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar
#el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía
#de autobuses y lo que debe pagar cada alumno por el viaje


alumnos = int(input("Introduce el número de alumnos: "))

if alumnos <= 0:
    print("Número de alumnos incorrecto")

elif alumnos >= 100:
    precio = 65
    pago = alumnos * precio

elif alumnos >= 50:
    precio = 70
    pago = alumnos * precio

elif alumnos >= 30:
    precio = 95
    pago = alumnos * precio

else:
    pago = 4000
    precio = pago / alumnos

print("Pago a la compañía:", pago, "euros")
print("Precio por alumno:", precio, "euros")