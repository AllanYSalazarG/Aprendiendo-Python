class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):  # Herencia
    def pasear(self):
        print("paseando")


class Chanchito(Perro):  # Herencia multinivel, no pasar de dos niveles (este es de un nivel)
    def programar(self):
        print("programando")
