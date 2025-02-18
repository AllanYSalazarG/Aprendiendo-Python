try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:  # Se ejecuta cuando hay errores
    print("Ingrese un valor que corresponda")
else:  # Se ejecuta cuando no hay errores
    print("No ocurrió ningún error")
finally:  # Se ejecuta siempre
    print("Se ejecuta siempre")
