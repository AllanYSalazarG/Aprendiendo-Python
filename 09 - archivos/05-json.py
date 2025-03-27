import json
from pathlib import Path

# Escribir json

# # creamos un listado de diccionarios que es practicamente la estructura de los json
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# # con json.dumps transformamos el listado de productos y pasamos a formato json
# data = json.dumps(productos)

# # creamos el archivo con la data
# Path("09 - archivos/productos.json").write_text(data)


# Leer json


data = Path("09 - archivos/productos.json").read_text(encoding="utf-8")
# carga la data a productos
productos = json.loads(data)
# print(productos)

# Modificar json
productos[0]["name"] = " Chanchito Feliz"
Path("09 - archivos/productos.json").write_text(json.dumps(productos))
