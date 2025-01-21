# Una tupla es igual que una lista, la diferencia es que no se pueden modificar las que ya existen

numeros = (1, 2, 3) + (4, 5, 6)

print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# Esto dará un error, ya que no se pueden modificar las tuplas
# numeros[0] = 5
