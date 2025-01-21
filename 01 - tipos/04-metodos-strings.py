animal = "  chaNCHito feliz  "
print(animal.upper())  # pasa todo a mayuscula
print(animal.lower())  # pasa todo a minuscula
print(animal.strip().capitalize())  # pone la primera letra en mayuscula
print(animal.title())  # pone la primera letra de cada palabra en mayuscula
# quita los espacios en ambos sentidos.
# tambien esta el metodo lstrip() y rstrip() para quitar espacios a la izquierda o derecha
print(animal.strip())
# busca una subcadena en la cadena, regresa la posicion de la primera letra de la subcadena
print(animal.find("cH"))
# reemplaza una cadena/caracter por otra
print(animal.replace("feliz", "triste"))
# busca una subcadena/caracter en la cadena, regresa True si está, False si no
print("NCH" in animal)
print("NCH" not in animal)  # Lo contrario a in, busca si no está
