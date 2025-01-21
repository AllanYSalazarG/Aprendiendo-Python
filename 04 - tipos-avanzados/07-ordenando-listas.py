numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# numeros.sort(reverse=True)  # Ordena la lista de menor a mayor | Reverse = True Ordena la lista de mayor a menor |
# Sorted crea una nueva lista ordenada y no modifica la lista original
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# Ordena por el primer elemento de la lista siempre y cuando tenga numeros al inicio
usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]


def ordena(elemento):
    return elemento[1]  # Ordena por el segundo elemento de la lista


usuarios.sort(key=ordena)
print(usuarios)


# Ordena por el primer elemento de la lista siempre y cuando tenga numeros al inicio
usuarios.sort(key=lambda el: el[1])
print(usuarios)
