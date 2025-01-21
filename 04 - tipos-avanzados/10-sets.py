# set significa grupo o conjunto
# Set = Coleccion de datos que no se puede repetir y no tiene orden

primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)
print(primer | segundo)  # Union: el operador "|" une los elementos de ambos sets
# Interseccion: el operador "&" muestra los elementos que estan en ambos sets
print(primer & segundo)
# Diferencia: el operador "-" muestra los elementos que estan en el primer set pero no en el segundo
print(primer - segundo)
# Diferencia simetrica: el operador "^" muestra los elementos que no estan en ambos sets
print(primer ^ segundo)
# primer.add(5)
# primer.remove(1)
# print(primer)
