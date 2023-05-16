import copy
import time
import random
from greedy_estocastico import leer_archivo, pretty_print, greedy_estocastico, costo
def hill_climbing_mejor_mejora(data):
    # Dado un orden estocastico, se intenta mejorar el orden de aterrizaje de los uavs
    # Para esto, se toma un uav y se mueve a la derecha hasta encontrar la mejor mejora de costo
    # Si el costo del nuevo orden es menor, se acepta el cambio
    # Si el costo del nuevo orden es mayor, se rechaza el cambio
    # Si el costo del nuevo orden es igual, se rechaza el cambio
    # Se retorna el mejor orden encontrado
    costo_actual = costo(data)
    mejor_orden = copy.deepcopy(data)
    n = 0
    print("costo actual: ", costo_actual)
    #print("orden actual: ")
    #pretty_print(mejor_orden)
    for i in range(len(mejor_orden)):
        n = i
        orden_actual = copy.deepcopy(mejor_orden)
        while n < len(orden_actual) - 1:
            #if n < len(orden_actual) - 1:  # Verifica que no sea el último elemento
                valor_actual = orden_actual[n]
                valor_siguiente = orden_actual[n+1]
                orden_actual[n] = valor_siguiente
                orden_actual[n+1] = valor_actual
                n += 1
                if costo(orden_actual) < costo_actual:
                    #print("posicion ",i," con valor ",valor_actual[0] , " se mueve a: ", n+1)
                        costo_actual = costo(orden_actual)
                        mejor_orden = copy.deepcopy(orden_actual)
            #else:
                #break
    print("costo final: ", costo_actual)
    
    #print("orden final: ")
    #pretty_print(mejor_orden)
    return mejor_orden

def pruebas(sorted_data):
    array = ["prueba 1", "prueba 2", "prueba 3", "prueba 4", "prueba 5"]
    pruebas = []
    for each in array:
        value = copy.deepcopy(sorted_data)
        pruebas.append(greedy_estocastico(value, each))
    return pruebas

uavs = leer_archivo("t2_Titan.txt")
sorted_data = sorted(uavs, key=lambda x: x[1][1])
estocastico = pruebas(sorted_data)
print("Hill Climbing mejor-mejora: ")
hill_climbing_mejor_mejora(estocastico[0])
print("------------------------------------")
hill_climbing_mejor_mejora(estocastico[1])
print("------------------------------------")
hill_climbing_mejor_mejora(estocastico[2])
print("------------------------------------")
hill_climbing_mejor_mejora(estocastico[3])
print("------------------------------------")
hill_climbing_mejor_mejora(estocastico[4])
print("------------------------------------")