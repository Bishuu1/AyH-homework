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
    Aterrizajes = []
    for each in sorted_data:
        if len(Aterrizajes) == 0:
            Aterrizajes.append(each)
        else:
            Aterrizajes.append(each)
    return Aterrizajes

def costo(aterrizajes):
    costo = 0
    reloj = 0
    for i, each in enumerate(aterrizajes):
        if i == 0:    
            reloj = each[1][1]
        if i != 0:
            tiempo_req = aterrizajes[i - 1][2][each[0] - 1]
            aterrizaje = max(each[1][1], reloj + tiempo_req)
            reloj = aterrizaje
            dif = abs(each[1][1] - reloj)
            costo += dif
            if reloj > each[1][2]:
                costo += 1000000
            elif reloj < each[1][0]:
                costo += 1000000
            
    return costo

greedy1 = greedy("t2_Titan.txt")
print("Costo para Titan: ", costo(greedy1))

greedy2 = greedy("t2_Europa.txt")
print("Costo para Europa: ", costo(greedy2))

greedy3 = greedy("t2_Deimos.txt")
print("Costo para Deimos: ", costo(greedy3))