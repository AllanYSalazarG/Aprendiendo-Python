nombre_curso = "Ultimate Python"
descripcion_curso = """Ultimate Python, este curso es el más completo de Python en español."""
print(nombre_curso, descripcion_curso)

print(len(nombre_curso))  # Longitud del string
# Primer caracter, al poner un indice, nos imprime el caracter en esa posición
print(nombre_curso[0])
print(nombre_curso[0:8])  # [Donde comienza:Donde termina] de leer el string
# Si no se pone el segundo valor, se toma hasta el final
print(nombre_curso[9:])
# Si no se pone el primer valor, se toma desde el principio
print(nombre_curso[:8])
print(nombre_curso[:])  # Si no se pone ningun valor, se toma todo el string
