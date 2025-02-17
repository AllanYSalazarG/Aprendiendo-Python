class Ave:  # Clase Padre
    def __init__(self):
        self.volador = "volador"

    def vuela(self):
        print("vuela ave")


class Pato(Ave):  # Clase Hijo
    def __init__(self):
        super().__init__()
        self.nada = "navador"

    def vuela(self):
        # super().vuela()  # super() nos trae los metodos de la clase padre
        print("vuela pato")


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
