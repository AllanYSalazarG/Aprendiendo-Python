class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def ladra(self):
        print(f"{self.__name} dice: Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito feliz", 4)


perro1 = Dog.factory()
perro1.ladra()
print(perro1.__dict__)
