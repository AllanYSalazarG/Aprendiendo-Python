class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Destructor
    def __del__(self):
        print(f"Chao {self.name}, te recordaremos")

    # Método mágico
    def __str__(self):
        return f"Clase Perro: {self.name}"

    # Método definido
    def ladra(self):
        print(f"{self.name}Guau!")


dog = Dog("Chanchito", 7)
del dog
