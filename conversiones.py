from sys import argv
from os import system

# Se almacenan datos en lista conversion
conversion = [float(argv[i]) for i in range(1, 4)]
print(conversion)
pesosChilenos = float(argv[4])


# Se almacena calculo de conversion en lista conversiones
conversiones = [pesosChilenos * convierte for convierte in conversion]
print(conversiones)

system('cls')

# Imprimir los resultados de las conversiones
print(f'Los {pesosChilenos} pesos equivalen a:')
print(f'{conversiones[0]} Soles')
print(f'{conversiones[1]} Pesos Argentinos')
print(f'{conversiones[2]} Dólares')