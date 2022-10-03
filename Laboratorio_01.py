# -*- coding: utf-8 -*-
#Nombre: Edwin Calle Perez
#Carrera: Ing. De Sistemas

import random

def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios):
# Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)
        
#Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1

#Se ubica una ficha de manera aleatoria
    ficha_fila = random.randrange(numero_filas)
    ficha_columnas = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = 'o'

    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
            numero_espacios_generados += 1
            
    return mapa_laberinto

n_filas = int(input('Introduzca el número de filas del laberinto: '))
n_columnas = int(input('Introduzca el número de columnas del laberinto: '))
numero_paredes = int(input('Introduzca el número de paredes del laberinto: '))
numero_espacios = n_filas * n_columnas - numero_paredes

laberinto = crear_mapa_laberinto(n_filas, n_columnas, numero_paredes, numero_espacios)

for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)
print("")

#MOVER FICHA
    
laberinto[n_filas - 1][len(laberinto[n_filas - 1]) - 1] = "S"

def despliegue_laberinto():
    for z in range(len(laberinto) - 1):
        print(str(laberinto[z]) +  ",")
    print(laberinto[len(laberinto) - 1])
despliegue_laberinto()

for i in range(n_filas):
    laberinto[i].append("#")
for i in range(n_filas):
    laberinto[i] = ["#"] + laberinto[i]
techo_y_suelo = [["#"]]
for i in range(n_columnas + 1):
    techo_y_suelo[0] += ["#"]
laberinto = techo_y_suelo + laberinto
laberinto += techo_y_suelo

i = 1
j = 1
movimientos = []
condicion = True
while condicion:
    laberinto[i][j] = "o"
    if laberinto[i + 1][j] == "S" or laberinto[i - 1][j] == "S" or laberinto[i][j+ 1] == "S" or laberinto[i - 1][j] == "S":
        if laberinto[i + 1][j] == "S":
            movimientos += ["Abajo"]
        elif laberinto[i - 1][j] == "S":
            movimientos += ["Arriba"]
        elif laberinto[i][j + 1] == "S":
            movimientos += ["Derecha"]
        elif laberinto[i][j - 1] == "S":
            movimientos += ["Izquierda"]
        break
    elif laberinto[i + 1][j] == " " or laberinto[i - 1][j] == " " or laberinto[i][j+ 1] == " " or laberinto[i - 1][j] == " ":
        if laberinto[i + 1][j] == " ":
            movimientos += ["Abajo"]
            i += 1
        elif laberinto[i - 1][j] == " ":
            movimientos += ["Arriba"]
            i -= 1
        elif laberinto[i][j + 1] == " ":
            movimientos += ["Derecha"]
            j += 1
        elif laberinto[i][j - 1] == " ":
            movimientos += ["Izquierda"]
            j -= 1
    else:
        laberinto[i][j] = "o"
        movimientos += ["Sin salida"]
        break

laberinto.pop()
laberinto.pop(0)
for c in range(min(n_columnas, n_filas)):
    laberinto[c].pop()
    laberinto[c].pop(0)
#Se elimina la capa de muros que se había añadido tras ya hacer el recorrido
print("")
despliegue_laberinto()
print(movimientos)