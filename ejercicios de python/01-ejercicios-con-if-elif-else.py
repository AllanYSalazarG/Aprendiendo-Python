"""Practicando con IF, ELIF y ELSE"""

import datetime

# 1. Escribe un programa que determine si un número es divisible por 3, 5 o ambos

# numero = int(input("Ingresa un número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"El número {numero} es divisible por 3 y 5")
elif numero % 5 == 0:
    print(f"El número {numero} es divisible por 5")
elif numero % 3 == 0:
    print(f"El número {numero} es divisible por 3")
else:
    print(f"El número {numero} no es divisible por 3 y 5")


# 2. Crea un programa que clasifique una nota en "Aprobado" o "Reprobado"
# según si es mayor o igual a 60

# notaAlumno = int(input("Ingresa la calificación del alumno: "))

if notaAlumno >= 60:
    print("APROBADO: El alumno ha aprobado la materia")
else:
    print("REPROBADO: El alumno tendrá que retomar la materia")

# 3. Escribe un programa que pida tres números y determine cuál es el mayor

numero1 = int(input("Ingresa el 1er número: "))
numero2 = int(input("Ingresa el 2er número: "))
numero3 = int(input("Ingresa el 3er número: "))

if numero1 > numero2:
    if numero1 > numero3:
        print(f"{numero1} es el número mayor")
    elif numero2 > numero3:
        print(f"{numero2} es el número mayor")
    else:
        print(f"{numero3} es el número mayor")
elif numero2 > numero3:
    print(f"{numero2} es el número mayor")
else:
    print(f"{numero3} es el número mayor")

# 4. Haz un programa que calcule el costo total de un producto con descuento según su precio inicial
# (descuento del 10%, 20% o 30% dependiendo del precio)

precioProducto = int(input("Costo del producto: "))

if precioProducto <= 100:
    costoTotalProducto = precioProducto - precioProducto * 0.1
    print(
        f"El producto tiene un descuento de 10%, dando un total de ${costoTotalProducto} pesos")
elif 101 < precioProducto < 200:
    costoTotalProducto = precioProducto - precioProducto * 0.2
    print(
        f"El producto tiene un descuento de 20%, dando un total de ${costoTotalProducto} pesos")
else:
    costoTotalProducto = precioProducto - precioProducto * 0.3
    print(
        f"El producto tiene un descuento de 30%, dando un total de ${costoTotalProducto} pesos")


# 5. Diseña un sistema que determine si un año es bisiesto

year = int(input("Ingresa un año: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"El año {year} es bisiesto")
        else:
            print(f"El año {year} no es bisiesto")
    else:
        print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")

# 6. Programa que reciba una letra y diga si es una vocal, una consonante o un símbolo

caracter = str(input("Ingresa un cáracter: "))
vocales = "aeiouAEIOU"

if caracter.isalpha():
    if caracter in vocales:
        print("Es una vocal")
    else:
        print("Es una consonante")
else:
    print("Es un caracter especial")

# 7. Escribe un programa que evalúe el puntaje de un examen y lo clasifique (A, B, C, D, o F)

calificacionExamen = int(input("Ingresa la calificación del exámen: "))

if calificacionExamen >= 60:
    if 91 <= calificacionExamen <= 100:
        print("El alumnó sacó una A")
    elif 81 <= calificacionExamen <= 90:
        print("El alumno sacó una B")
    elif 71 <= calificacionExamen <= 80:
        print("El alumno sacó una C")
    else:
        print("El alumno sacó una D")
else:
    print("El alumno sacó una F")

# 8. Haz un programa que determine si un usuario puede ingresar un sitio web según su edad y país

edadUsuario = int(input("Ingresa tu edad: "))
paisUsuario = str(input("Ingresa tu país (MX, US, AR, PU, UK, KN, AF): "))
paisUsuario = paisUsuario.upper()
paisesPermitidos = ["MX", "AR", "PU", "CA"]

if edadUsuario >= 18:
    if paisUsuario in paisesPermitidos:
        print("Sitio web accedido")
    else:
        print("No puedes acceder al sitio web")
else:
    print("No puedes acceder al sitio web")

# 9. Crea un programa que tome la hora actual y devuelva "Buenos días", "Buenas tardes"
# o "Buenas noches"

# Buenos días: 5:00 a las 11:59
# Buenas tardes: 12:00 a las 18:59
# Buenas noches: 19:00 a las 4:59

horaActual = datetime.datetime.now()

hora = horaActual.hour
minuto = horaActual.minute
segundo = horaActual.second

print(f"Hora: {hora}")
print(f"Minuto: {minuto}")
print(f"Segundo: {segundo}")

if 5 <= horaActual.hour <= 11:
    print("Buenos días")
elif 12 <= horaActual.hour <= 18:
    print("Buenos tardes")
elif 19 <= horaActual.hour <= 23:
    print("Buenos noches")
else:
    print("Buenas noches")

# 10. Diseña un sistema de clasificación de películas por edades
# (Ej.: Infantil, Adolescente, Adulto)

edad = int(input("Ingresa tu edad"))

if edad >= 18:
    print("Puedes ver la película de adultos")
elif edad >= 14:
    print("Puedes ver la película para adolescentes")
else:
    print("Solo puedes ver películas para niños")
