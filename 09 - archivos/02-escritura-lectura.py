from pathlib import Path

archivo = Path("09 - archivos/archivo-prueba.txt")
# con .read_text() leemos el contenido del archivo tal cual está
# debemos agregar un tipo de codificación (por lo general utf-8)
texto = archivo.read_text("utf-8").split("\n")
# agregando split() podremos separar el contenido como queramos para que se agregue en una lista

texto.insert(0, "hola mundo")
# write_text() agrega data al archivo
# Hay que tener CUIDADO ya que si tiene data dentro y le agregamos mas,
# la data que ya está dentro se borra y se agrega la nueva.

# Si queremos mantener la data y agregar la nueva
# debemos manipular toda la info ya existente (haciendo lo de arriba practicamente)
archivo.write_text("\n".join(texto), "utf-8")
print(texto)
