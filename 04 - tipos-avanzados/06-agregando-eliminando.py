mascotas = ["Wolfgang", "Pelusa", "Pulga",
            "Felipe", "Pulga", "Chanchito Feliz"]

mascotas.insert(1, "Melvin")  # Agrega un elemento en la posición 1
mascotas.append("Chanchito Triste")  # Agrega un elemento al final

mascotas.remove("Pulga")  # Elimina la primera ocurrencia de "Pulga"
mascotas.pop()  # Elimina el último elemento
mascotas.pop(1)  # Elimina el elemento en la posición 1
del mascotas[0]  # Elimina el elemento en la posición 0
mascotas.clear()  # Elimina todos los elementos
print(mascotas)
