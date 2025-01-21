# and, or, not

gas = False
encendido = True
edad = 18

# if not gas and (encendido or edad > 17):
#     print("Puedes avanzar")
# else:
#     print("No puedes avanzar")


# corto circuito

# and: si el primer valor es falso, no se evalua el segundo
# or: si el primer valor es verdadero, no se evalua el segundo

if not gas and encendido and edad > 17:
    print("Puedes avanzar")
else:
    print("No puedes avanzar")
