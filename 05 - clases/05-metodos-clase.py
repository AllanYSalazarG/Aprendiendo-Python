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

    # Classmethod transforma los metodos a metodos de clase
    # se cambia self por cls
    @classmethod
    def ladra(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


Dog.ladra()
perro1 = Dog("Chanchito", 2)
perro2 = Dog("Felipe", 3)
perro3 = Dog.factory()
print(perro3.age, perro3.name)
