print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, resta, multi y div")
opcion = ""
num1 = float(input("Ingresa un número: "))
while opcion.lower() != "salir":
    opcion = input("Escribe la operación: ")
    if opcion.lower() == "salir":
        print("Adios")
        break
    num2 = float(input("Ingresa siguiente número: "))
    if opcion == "suma":
        resultado = num1 + num2
        num1 = resultado
    elif opcion == "resta":
        resultado = num1 - num2
        num1 = resultado
    elif opcion == "multi":
        resultado = num1 * num2
        num1 = resultado
    elif opcion == "div":
        resultado = num1 / num2
        num1 = resultado
    else:
        print("Ingresa una operación válida")
    print(f"El resultado es {resultado} ")
