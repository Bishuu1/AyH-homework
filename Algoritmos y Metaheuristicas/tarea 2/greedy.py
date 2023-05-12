# Para algoritmo greedy tomaremos el mejor caso posible para cada uno en orden y en caso contrario tomaremos el siguiente mejor caso posible.

import copy
import time
import random
import numpy as np


# Obtener datos desde archivo t2_Deimos.txt
def leer_archivo(doc):
    # Reemplaza "datos.txt" con la ruta y nombre de tu archivo
    archivo = open(doc, "r")
    lineas = archivo.readlines()
    num_naves = int(lineas[0])
    uavs = []  # uav tiene 3 elementos: id, limites timpo y tiempos requeridos
    limites_tiempo = []
    tiempos_requeridos = []
    indice = 1  # indice para recorrer lineas
    for i in range(num_naves):
        count = 0
        limite = list(map(int, lineas[indice].split()))
        # limites_tiempo.append(limite)  # limite de tiempo (min, pref, max)
        indice += 1
        tiempos = list(map(int, lineas[indice].split()))
        tiempos_requeridos.append(tiempos)
        count += len(tiempos)
        while count < num_naves:
            indice += 1
            tiempos = list(map(int, lineas[indice].split()))
            tiempos_requeridos[i] += tiempos
            count += len(tiempos)
        indice += 1
        uavs.append([i + 1, limite, tiempos_requeridos[i]])
    archivo.close()
    return uavs


def pretty_print(arr):
    for item in arr:
        print(item)


# Algoritmo Greedy
def greedy(archivo):
    # Ordenar tiempos preferidos de menor a mayor
    uavs = leer_archivo(archivo)
    sorted_data = sorted(uavs, key=lambda x: x[1][1])

    # Ahora, con los datos ordenados procederemos a asignar el aterrizaje de cada UAV en tiempo preferido en caso de ser posible, es decir, si el tiempo preferido es mayor o igual al tiempo del aterrizaje anterior más el tiempo de espera del UAV.
    # En caso contrario, se asignará el siguiente mejor tiempo posible.
    # Para esto, se creará una lista de lanzamientos que se irá llenando conforme se asignen los lanzamientos de los UAVs.
    # UAVs = [id, [min, pref, max], [tiempos requeridos]]

    # [id, tiempo de aterrizaje, diferencia tiempo preferido y tiempo de aterrizaje]
    Aterrizajes = ([])
    costo = 0
    for each in sorted_data:
        if len(Aterrizajes) == 0:
            Aterrizajes.append([each[0], each[1][1], 0])
            tiempos = each[2]
            # guardar tiempos requeridos para iteración siguiente ocuparlos para calcular costo y tiempo de aterrizaje
        else:
            # maximo entre tiempo preferido y tiempo de aterrizaje anterior + tiempo requerido
            Aterrizajes.append(
                [each[0], max(each[1][1], Aterrizajes[-1][1] + tiempos[each[0] - 1])])

            Aterrizajes[-1].append(abs(Aterrizajes[-1][1] - each[1][1]))

            # costo es la diferencia entre tiempo preferido y tiempo de aterrizaje real
            costo += abs(Aterrizajes[-1][1] - each[1][1])
            tiempos = each[2]
    print("Costo: ", costo)
    print("Aterrizajes: ", Aterrizajes)


greedy("t2_Titan.txt")
