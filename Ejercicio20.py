#Ejercicio 20
#Una compañía de transporte internacional tiene servicio en algunos países de América del
#Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de
#transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se
#muestra en la tabla:
#khadija
#fecha:5-11-2026


peso = float(input("Introduce el peso del paquete en kg: "))
zona = int(input("Introduce la zona (1-5): "))

if peso <= 0:
    print("Peso incorrecto")

elif peso > 5:
    print("El paquete no puede transportarse")

elif zona == 1:
    precio = 24

elif zona == 2:
    precio = 20

elif zona == 3:
    precio = 21

elif zona == 4:
    precio = 10

elif zona == 5:
    precio = 18

else:
    precio = 0
    print("Zona incorrecta")

if peso > 0 and peso <= 5 and zona >= 1 and zona <= 5:
    gramos = peso * 1000
    total = gramos * precio
    print("Precio del transporte:", total, "euros")