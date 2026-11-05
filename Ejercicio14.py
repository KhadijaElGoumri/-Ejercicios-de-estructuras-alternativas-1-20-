#Ejercicio 14
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la
#cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta
#del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
#productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo
#A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es
#de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
#cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.


precio = float(input("Introduce el precio inicial por kilo: "))
tipo = input("Introduce el tipo (A/B): ").upper()
tamano = int(input("Introduce el tamaño (1/2): "))
kilos = float(input("Introduce los kilos de uva: "))

if tipo == "A" and tamano == 1:
    precio = precio + 0.20

elif tipo == "A" and tamano == 2:
    precio = precio + 0.30

elif tipo == "B" and tamano == 1:
    precio = precio - 0.30

elif tipo == "B" and tamano == 2:
    precio = precio - 0.50

else:
    print("Tipo o tamaño incorrecto")
    precio = -1

if precio >= 0 and kilos > 0:
    ganancia = precio * kilos
    print("Ganancia:", ganancia, "euros")