from pathlib import Path
from zipfile import ZipFile

with ZipFile("09 - archivos/comprimidos.zip", "w") as zip:
    # Aprendiendo-Python (Carpeta raiz)
    # Esto es para seleccionar todo lo que está dentro de Aprendiendo-Python
    # for path in Path().rglob("*.*"):
    # aqui seleccionamos todo lo que esta pero dentro de "09 - archivos"
    for path in Path().rglob("09 - archivos/*.*"):
        print(path)
        if str(path) != "09 - archivos/comprimidos.zip":
            zip.write(path)
