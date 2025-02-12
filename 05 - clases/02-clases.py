class Perro:
    def ladra(self):
        print("Guau!")


mi_perro = Perro()
mi_perro.ladra()
# isinstance verifica si un objeto pertenece a una clase isinstance(objeto, clase)
print(isinstance(mi_perro, Perro))
