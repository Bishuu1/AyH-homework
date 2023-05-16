import random
import time
import random

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

def calcular_diferencia(tiempo_preferido, tiempo_real):
    return tiempo_preferido - tiempo_real

def algoritmo_greedy_estocastico(archivo):
    datos = leer_archivo(archivo)
    uavs = sorted(datos, key=lambda x: x[1][1])
    
    uavs_ordenados = []  # Lista para almacenar los uavs ordenados
    costo_total = 0

    while len(uavs) > 0:
        uav_seleccionado = random.choice(uavs)  # Selecciona un uav aleatorio
        uavs.remove(uav_seleccionado)  # Remueve el uav seleccionado de la lista original

        # Calcula el tiempo real de aterrizaje sumando el tiempo de ocupación de la pista de los uavs anteriores
        tiempo_real = uav_seleccionado[1][0]  # Tiempo mínimo de aterrizaje del uav seleccionado

        if len(uavs_ordenados) > 0:
            ultimo_uav = uavs_ordenados[-1]
            tiempo_real += ultimo_uav[2][ultimo_uav[0] - 1]  # Agrega el tiempo de ocupación del uav anterior

        # Calcula la diferencia entre el tiempo preferido y el tiempo real de aterrizaje
        diferencia = calcular_diferencia(uav_seleccionado[1][1], tiempo_real)

        # Busca la posición de inserción en la lista ordenada que minimice la diferencia
        posicion_insercion = 0
        mejor_diferencia = diferencia

        for i, uav in enumerate(uavs_ordenados):
            tiempo_anterior = uav[2][uav[0] - 1]  # Tiempo de ocupación del uav anterior en la lista ordenada
            nueva_diferencia = calcular_diferencia(uav_seleccionado[1][1], tiempo_real + tiempo_anterior)

            if nueva_diferencia < mejor_diferencia:
                posicion_insercion = i + 1
                mejor_diferencia = nueva_diferencia

        # Inserta el avión seleccionado en la posición de inserción
        uavs_ordenados.insert(posicion_insercion, uav_seleccionado)

    # Imprimir información de los UAVs ordenados
    for uav in uavs_ordenados:
        uav_id = uav[0]
        tiempo_aterrizaje = uav[1][0] + sum(uavs_ordenados[i][2][uavs_ordenados[i][0] - 1] for i in range(uav_id - 1))
        diferencia = calcular_diferencia(uav[1][1], tiempo_aterrizaje)
        print(f"UAV {uav_id}: Tiempo de aterrizaje = {tiempo_aterrizaje}, Diferencia = {diferencia}")

        costo_total += diferencia

    print(f"Costo total: {costo_total}")

algoritmo_greedy_estocastico("t2_Titan.txt")