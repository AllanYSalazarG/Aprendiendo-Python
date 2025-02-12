class Dog:
    """ __init__ es el constructor de la clase
     Aqui es donde agregamos los atributos que tendrá
      cada instancia / objeto """
    # self se refiere a la instancia misma. Ejemplo: mi_perro

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ladra(self):
        print(f"{self.name} dice: Guau!")


mi_perro = Dog("Chanchito", 1)
mi_perro.ladra()
print(mi_perro.name)
mi_perro.ladra()
# isinstance verifica si un objeto pertenece a una clase isinstance(objeto, clase)
print(isinstance(mi_perro, Dog))
