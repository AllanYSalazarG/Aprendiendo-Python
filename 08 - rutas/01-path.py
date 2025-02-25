from pathlib import Path

# Path(r"C:\Archivos de Programa\Minecraft")
# Path("/usr/bin")  # Ruta Absoluta
# Path()
# Path.home()
# Path("one/__init__.py")  # Ruta Relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,  # Nombre del archivo con extensión
    path.stem,  # Nombre del archivo sin extensión
    path.suffix,  # Extensión del archivo
    path.parent,  # Carpeta padre (Donde se encuentra el archivo)
    path.absolute()  # La ruta donde se pudiera encontrar el archivo
)

# Nos deja cambiar el nombre del archivo y su extensión
p = path.with_name("chanchito.exe")
print(p)
p = path.with_suffix(".bat")
print(p)
p = path.with_stem("feliz")
print(p)
