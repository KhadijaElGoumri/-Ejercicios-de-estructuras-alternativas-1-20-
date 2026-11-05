#Ejercicio 13
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.


dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

if mes < 1 or mes > 12 or anio < 1:
    print("Fecha incorrecta")

else:
    if mes == 2:
        if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
            dias = 29
        else:
            dias = 28

    elif mes in [4, 6, 9, 11]:
        dias = 30

    else:
        dias = 31

    if dia >= 1 and dia <= dias:
        print("Fecha correcta")
    else:
        print("Fecha incorrecta")