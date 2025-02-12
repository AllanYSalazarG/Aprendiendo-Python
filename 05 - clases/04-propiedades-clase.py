class Dog:
    """ __init__ es el constructor de la clase
     Aqui es donde agregamos los atributos que tendrá
      cada instancia / objeto """
    # Estas propiedades se asignan a todas las instancias
    # Si se modifica, se modifica en todas las instancias
    # a menos que modifiques solo la instancia. Ejemplo: mi_perro.patas = 5
    patas = 4
    # self se refiere a la instancia misma. Ejemplo: mi_perro

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ladra(self):
        print(f"{self.name} dice: Guau!")


mi_perro = Dog("Chanchito", 1)
mi_perro.patas = 5
mi_perro2 = Dog("Felipe", 1)
print(Dog.patas)
print(mi_perro.patas)
print(mi_perro2.patas)
