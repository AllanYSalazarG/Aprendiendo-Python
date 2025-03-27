from io import open


# Escritura

# texto = "Hola Mundo"

# # open() abre el archivo, el primer parametro es la ruta del archivo
# # el segundo parametro es el tipo de accion "w" es escritura "r" es lectura
# # esta accion crea el archivo si es que no existe
# archivo = open("09 - archivos/hola.txt", "w")
# archivo.write(texto)
# # cuando terminemos de usar el archivo, hay que cerrarlo con .close()
# # para que no gaste recursos de la computadora
# archivo.close()


# Lectura

# # para leer, se agrega el "r" aunque si no se agrega, queda implicito, es default
# archivo = open("09 - archivos/hola.txt", "r")
# # read() para leer el archivo
# texto = archivo.read()
# archivo.close()
# print(texto)


# Lectura como lista

# # para leer, se agrega el "r" aunque si no se agrega, queda implicito, es default
# archivo = open("09 - archivos/hola.txt", "r")
# # readlines() para leer el archivo y devolver a texto como lista
# texto = archivo.readlines()
# archivo.close()
# print(texto)


# metodos magicos

# with y seek

# # con with no es necesario usar el close() porque tiene
# # los metodos __enter__ y __exit__ que se encargan de hacerlo automaticamente
# with open("09 - archivos/hola.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)
# # cuando usamos el readlines() y el for, solo leerá una vez el archivo
# # porque no se devuelve al primer caracter del mismo
# # para eso se necesita el seek(0) donde 0 es el primer caracter
# # del contenido del archivo


# Agregar

# # con "a+" agregamos datos al archivo sin que se borre el ya existente
# archivo = open("09 - archivos/hola.txt", "a+")
# archivo.write("Chao mundo")
# archivo.close()


# Lectura y Escritura

with open("09 - archivos/hola.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    # writelines() escribe el texto que queremos agregar
    # pero si hay texto ya existente y empezamos a escribir
    # desde el comienzo como se hace ahora,
    # el nuevo texto sobreescribira el antiguo (como cuando presionamos INSERT en el teclado)
    archivo.writelines(texto)
