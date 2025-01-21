from pprint import pprint

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes.

cadena = "si se puede"


def quitarEspacios(cadena):
    return [caracter for caracter in cadena if caracter != " "]


# 2. Contar en un diccionario cuanto se repiten los caracteres de un string.


def contarCaracteres(cadena):
    diccionario = {}
    for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario

# 3. Ordenar las llaves de un diccionario por el valor que tienen y devolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c",4)]


def ordenarElementos(diccionario):
    lista = []
    for elemento in diccionario.items():
        lista.append(elemento)
    return sorted(lista, key=lambda elemento: elemento[1], reverse=True)

# 4. De un listado de tuplas, devolver las tuplas que tengan el mayor valor


def elementoMayor(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten con # repeticiones son:
# - Caracter
# - Caracter


def mensajeCaracteresRepetidos(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones"
    return mensaje

# Llamando a las funciones


cadenaSinEspacios = quitarEspacios(cadena)
caracteresContados = contarCaracteres(cadenaSinEspacios)
listaOrdenada = ordenarElementos(caracteresContados)
elMayor = elementoMayor(listaOrdenada)
mensaje = mensajeCaracteresRepetidos(elMayor)

print(mensaje)
