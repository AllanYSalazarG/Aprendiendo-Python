import csv
import os

# Escribir

# # newline="" sirve para que no haya saltos de linea
# # al escribir el archivo, al final de writerow()
# # agregaba un salto de linea viendose en excel y visual studio
# with open("09 - archivos/archivo.csv", "w", newline="") as archivo:
#     # se crea una instancia de csv.writer() para poder
#     # escribir en el
#     writer = csv.writer(archivo)
#     # writerow() escribe un registro al csv
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "este es un twit"])
#     writer.writerow([1001, 2, "otro twit"])


# Lectura

# with open("09 - archivos/archivo.csv") as archivo:
#     # creamos reader atravez de csv.reader() para poder leerlo
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)


# Actualizar CSV


# Para esto necesitamos leer el archivo existente y crear uno temporal para guardar la data del 1er archivo

with open("09 - archivos/archivo.csv") as r, open("09 - archivos/archivo_temp.csv", "w", newline="") as w:
    # archivo viejo lo leemos
    reader = csv.reader(r)
    # archivo temp le escribimos lo del archivo viejo
    writer = csv.writer(w)
    # leemos cada linea del archivo original
    for linea in reader:
        # validamos cual es el string que estamos buscando
        if linea[0] == "1000":
            # si sale verdadero, escribimos lo nuevo al archivo temporal
            # que en realidad solo escribimos el ultimo valor, el resto debe estar igual
            writer.writerow([1000, 1, "texto modificado"])
        else:
            # de lo contrario, agregamos al archivo temporal la linea tal cual
            writer.writerow(linea)

# con import os y os.remove(ruta del archivo) eliminamos el archivo
os.remove("09 - archivos/archivo.csv")
# con os.rename(ruta del archivo con nombre viejo, ruta del archivo con nuevo nombre)
os.rename("09 - archivos/archivo_temp.csv", "09 - archivos/archivo.csv")
