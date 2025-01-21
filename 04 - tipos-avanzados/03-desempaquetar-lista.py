numeros = [1, 2, 3]

# Desempaquetar lista FEO!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# Desempaquetar lista BONITO!
# primero, segundo, tercero = numeros
# print(primero, segundo, tercero)

# Desempaquetar lista BONITO! (con * para los demás)
primero, *otros, ultimo = numeros

print(primero, ultimo, otros)
