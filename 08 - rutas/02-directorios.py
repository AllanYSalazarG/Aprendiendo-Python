from pathlib import Path

path = Path("08 - rutas")

# path.exists()  # Existe?
# path.mkdir()  # Crea carpeta
# path.rmdir()  # Elimina carpeta si no tiene archivos
# path.rename("chanchito-feliz")  # Cambia el nombre del directorio

# for p in path.iterdir():  # Regresa las rutas / archivos que se encuentran dentro de la carpeta especificada "08 - rutas"
#     print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("01-*.py")]
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
