n1 = input("Ingresa el primero numero: ")
n2 = input("Ingresa el segundo numero: ")

n1 = int(n1)
n2 = int(n2)
# print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
Para los numeros {n1} y {n2} 
el resultado de la suma es {suma}, 
de la resta es {resta}, 
de la multiplicacion es {multiplicacion} 
y de la division es {division}"""

print(mensaje)
