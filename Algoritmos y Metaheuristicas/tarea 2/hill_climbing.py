import copy
import time
import random
from greedy_estocastico import leer_archivo, pretty_print, greedy_estocastico, costo

def hill_climbing_alguna_mejora(data):
    # Dado un orden estocastico, se intenta mejorar el orden de aterrizaje de los uavs
    # Para esto, se toma un uav y se mueve a la derecha hasta encontrar una mejora de costo
    # Si el costo del nuevo orden es menor, se acepta el cambio
    # Si el costo del nuevo orden es mayor, se rechaza el cambio
    # Si el costo del nuevo orden es igual, se acepta el cambio
    # Se repite el proceso hasta que no se pueda mejorar el orden
    # Se retorna el mejor orden encontrado
    costo_actual = costo(data)
    mejor_orden = copy.deepcopy(data)
    n = 0
    print("costo actual: ", costo_actual)
    print("orden actual: ")
    pretty_print(mejor_orden)
    for i in range(len(mejor_orden)):
        n = i
        orden_actual = copy.deepcopy(mejor_orden)
        flag = True
        while flag:
            if n < len(orden_actual) - 1:  # Verifica que no sea el último elemento
                valor_actual = orden_actual[n]
                valor_siguiente = orden_actual[n+1]
                orden_actual[n] = valor_siguiente
                orden_actual[n+1] = valor_actual
                n += 1
                if costo(orden_actual) < costo_actual:
                    print("posicion ",i," con valor ",valor_actual[0] , " se mueve a: ", n+1)
                    costo_actual = costo(orden_actual)
                    mejor_orden = copy.deepcopy(orden_actual)
                    flag = False
            else:
                break
    print("costo final: ", costo_actual)
    
    #print("orden final: ")
    pretty_print(mejor_orden)
    return mejor_orden



uavs = leer_archivo("t2_Titan.txt")
sorted_data = sorted(uavs, key=lambda x: x[1][1])
estocastico = greedy_estocastico(sorted_data)
hill_climbing_alguna_mejora(estocastico)