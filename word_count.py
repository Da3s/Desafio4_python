from os import system

# Importar el texto
print("")
with open("C:\\Users\\ztyle\\Dropbox\\BootCamp\\Desarrollo\\Modulo_Python\\Desafio4\\lorem_ipsum.txt", "r") as file:
    texto = file.read()
print(texto)

#separando texto en caracteras
#creo una lista con los caracteres dentro del texto
caracteres = [caracter for caracter in texto]
print(caracteres)

#Transformo la lista en set para eliminar elementos duplicados
set_caracter = set(caracteres)
print(set_caracter)

#Contando la cantidad de palabras
cantidad_caracteres = len(set_caracter)
print(cantidad_caracteres)



#separando el texto en palabras.
palabras = texto.split()
print(palabras) #el resultado se muestra en una lista


#Transformo lista a Set para eliminar elementos duplicados
set_palabras = set(palabras)
print(set_palabras)

#Contando la cantidad de palabras
cantidad_palabras = len(set_palabras)

system('cls')

print(f"El número de caracteres distintos es: {cantidad_caracteres}")
print(f"El número de palabras distintas es: {cantidad_palabras}")