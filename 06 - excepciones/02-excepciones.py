try:
    n1 = int(input("Ingresa primer número: "))
except ValueError as e:
    print("Ingrese un valor que corresponda")
except NameError as e:
    print("Ocurrio un error!")
