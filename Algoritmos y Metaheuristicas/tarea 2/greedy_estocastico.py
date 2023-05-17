# Para algoritmo greedy estocastico tomaremos el mejor caso posible para cada uno en orden y en caso contrario tomaremos el siguiente mejor caso posible con una probabilidad de 0.5.

import copy
import time
import random
import numpy as np

# Obtener datos desde archivo
def leer_archivo(doc): #esta vez con el reciproco
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

# Algoritmo Greedy estocastico
def greedy_estocastico(data, seed):   
    orden_estocastico = []
    costo = 0
    random.seed(seed)
    # Ahora, con los datos ordenados procederemos a asignar el aterrizaje de cada UAV dada una probabilidad de 0.5, en caso de no elegirse se pasa a al siguiente uav, así sucesivamente hasta haber introducido todos los uavs.
    while(data):
        for i in data:
            dato = data.pop(0)
            if random.random() < 0.5:
                orden_estocastico.append(dato)
            else:
                data.append(dato)
    return orden_estocastico

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

def pruebas(sorted_data):
    array = ["prueba 1", "prueba 2", "prueba 3", "prueba 4", "prueba 5"]
    pruebas = []
    for each in array:
        value = copy.deepcopy(sorted_data)
        pruebas.append(greedy_estocastico(value, each))
    return pruebas

#Titan
def titan():
    print("Titan: ")
    uavs = leer_archivo("t2_Titan.txt")
    sorted_data = sorted(uavs, key=lambda x: x[1][1])
    prueba = pruebas(sorted_data)

    return prueba

#Europa
def europa():
    print("Europa: ")
    uavs = leer_archivo("t2_Europa.txt")
    sorted_data = sorted(uavs, key=lambda x: x[1][1])
    prueba = pruebas(sorted_data)

    return prueba

#Deimos
def deimos():
    print("Deimos: ")
    uavs = leer_archivo("t2_Deimos.txt")
    sorted_data = sorted(uavs, key=lambda x: x[1][1])
    prueba = pruebas(sorted_data)

    return prueba

if __name__ == "__main__":
    titans_aterrizaje = titan()
    for i, each in enumerate(titans_aterrizaje):
        print("Costo de prueba ",i,": ",  costo(each))
    print("------------------------------------")
    europa_aterrizaje = europa()
    for i, each in enumerate(europa_aterrizaje):
        print("Costo de prueba ",i,": ",  costo(each))
    print("------------------------------------")
    deimos_aterrizaje = deimos()
    for i, each in enumerate(deimos_aterrizaje):
        print("Costo de prueba ",i,": ",  costo(each))
    print("------------------------------------")