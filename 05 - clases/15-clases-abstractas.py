# Obligatorio para poder usar clases abstractas
# Paso 1, agregando ABC y abstractmethod desde abc
from abc import ABC, abstractmethod

""" 
PASOS PARA HACER UNA CLASE ABSTRACTA

1. Importar ABC y abstractmethod desde abc
2. Heredar de ABC a la clase que queremos hacer abstracta
3. Agregar @property al metodo que queremos hacer abstracto
4. Agregar @abstractmethod al mismo metodo, seguido de @property
 """


class Model(ABC):  # Paso 2, para que clase model sea abstracta
    # def __init__(self):
    #     if not self.tabla:
    #         print("Error, tienes que definir una tabla")

    @property  # Paso 3. Agregando @property
    @abstractmethod  # Paso 4. Agregando @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        # print(f"Guardando {self.tabla} en BBDD")
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(1)
