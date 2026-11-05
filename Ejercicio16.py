#Ejercicio 16
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el
#cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan
#1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir
#del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es
#domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice
#un algoritmo para determinar cuánto debe pagar por cada concepto una persona que
#realiza una llamada


minutos = float(input("Introduce los minutos de llamada: "))
dia = input("¿Es domingo? (si/no): ").lower()
turno = input("Introduce el turno (mañana/tarde): ").lower()

if minutos <= 0:
    print("Duración incorrecta")

else:
    if minutos <= 5:
        coste = minutos * 1

    elif minutos <= 8:
        coste = 5 * 1 + (minutos - 5) * 0.80

    elif minutos <= 10:
        coste = 5 * 1 + 3 * 0.80 + (minutos - 8) * 0.70

    else:
        coste = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50

    if dia == "si":
        impuesto = coste * 0.03

    elif turno == "mañana":
        impuesto = coste * 0.15

    elif turno == "tarde":
        impuesto = coste * 0.10

    else:
        impuesto = 0

    total = coste + impuesto

    print("Coste de la llamada:", coste, "euros")
    print("Impuesto:", impuesto, "euros")
    print("Total a pagar:", total, "euros")