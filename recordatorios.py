recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# Se añade nueva fecha 2 de Febrero 2021 a la lista entregada
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])


# Se busca por fecha dentro de la lista para encontrar fecha mal ingresada, si la encuentra la reemplaza por la correcta
for fecha in recordatorios:
    if fecha[0] == '2021-07-15':
        fecha[0] = '2021-07-16'
        

# Se elimina dia del trabajo
for fecha in recordatorios:
    if fecha[0] == '2021-07-15':
        recordatorios.pop(2)     


# Se añaden cena de navidad y de año nuevo
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])


# Se ordenan de forma ascendente
recordatorios.sort()

# Output
print(recordatorios)
