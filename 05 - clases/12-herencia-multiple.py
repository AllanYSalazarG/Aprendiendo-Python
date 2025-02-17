class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")


class Perro(Caminador, Nadador):  # Herencia multiple.
    def programar(self):
        print("programando")
    # Si varias clases tienen el mismo metodo, se ejecutará el metodo de la primer clase (izquierda)
    # Para evitar esto, es necesario crear clases lo mas exclusivas posibles y eliminar los metodos
    # más comunes
