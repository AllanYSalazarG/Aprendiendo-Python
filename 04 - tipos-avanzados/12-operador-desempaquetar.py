lista = [1, 2, 3, 4, 5]
# print(1, 2, 3, 4, 5)
# print(*lista) # Esto se puede hacer con las listas o las tuplas

lista2 = [6, 7]
combinada = [*lista, *lista2]
print(combinada)

punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 20}
nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "hola"}
print(nuevoPunto)
