from pathlib import Path
from time import ctime

archivo = Path("09 - archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()

archivo.stat()

# fecha que accedemos al archivo
print("acceso", ctime(archivo.stat().st_atime))
# fecha que se crea el archivo
print("creación", ctime(archivo.stat().st_ctime))
# fecha cuando se modifica el archivo
print("modificación", ctime(archivo.stat().st_mtime))
