from pathlib import Path
from zipfile import ZipFile

# Escribir archivos comprimidos

# with ZipFile("09 - archivos/comprimidos.zip", "w") as zip:
#     # Aprendiendo-Python (Carpeta raiz)
#     # Esto es para seleccionar todo lo que está dentro de Aprendiendo-Python
#     # for path in Path().rglob("*.*"):
#     # aqui seleccionamos todo lo que esta pero dentro de "09 - archivos"
#     for path in Path().rglob("09 - archivos/*.*"):
#         print(path)
#         if str(path) != "09 - archivos/comprimidos.zip":
#             # write() agrega los archivos carpetas a comprimirse
#             zip.write(path)


# Leer archivos comprimidos

with ZipFile("09 - archivos/comprimidos.zip") as zip:
    # namelist() nos muestra los nombres de carpetas y archivos dentro del archivo comprimido
    # print(zip.namelist())
    # getinfo() nos devuelve información del archivo
    info = zip.getinfo("09 - archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )
    # extractall() nos extrae todo lo que tenga el archivo comprimido
    zip.extractall("09 - archivos/descomprimidos")
