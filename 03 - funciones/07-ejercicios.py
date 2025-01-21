def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    for _ in range(0, len(texto)):
        if texto[_] != texto[-_-1]:
            return False
    return True


print(es_palindromo("anita lava la tina"))
print(es_palindromo("hola mundo"))
print(es_palindromo("abba"))
