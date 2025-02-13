class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Clase Perro: {self.name}"

    def ladra(self):
        print(f"{self.name}Guau!")


dog = Dog("Chanchito", 7)
print(dog)
text = str(dog)
print(text)
