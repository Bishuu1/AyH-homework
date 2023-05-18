import copy
import time
import random
from greedy_estocastico import costo, europa, titan, deimos
from greedy import titan_greedy, europa_greedy, deimos_greedy
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


#Titan greedy
print("------------------------------------")
titan_greedy = titan_greedy()
print("Hill Climbing mejor-mejora: ")
hill_climbing_mejor_mejora(titan_greedy)
print("------------------------------------")
#Europa greedy
europa_greedy = europa_greedy()
print("Hill Climbing mejor-mejora: ")
hill_climbing_mejor_mejora(europa_greedy)
print("------------------------------------")
#Deimos greedy
deimos_greedy = deimos_greedy()
print("Hill Climbing mejor-mejora: ")
hill_climbing_mejor_mejora(deimos_greedy)
print("------------------------------------")
#Titan
titan = titan()
print("Hill Climbing mejor-mejora: ")
hill_climbing_mejor_mejora(titan[0])
print("------------------------------------")
hill_climbing_mejor_mejora(titan[1])
print("------------------------------------")
hill_climbing_mejor_mejora(titan[2])
print("------------------------------------")
hill_climbing_mejor_mejora(titan[3])
print("------------------------------------")
hill_climbing_mejor_mejora(titan[4])
print("------------------------------------")

#Europa
europa = europa()
print("Hill Climbing mejor-mejora: ")
hill_climbing_mejor_mejora(europa[0])
print("------------------------------------")
hill_climbing_mejor_mejora(europa[1])
print("------------------------------------")
hill_climbing_mejor_mejora(europa[2])
print("------------------------------------")
hill_climbing_mejor_mejora(europa[3])
print("------------------------------------")
hill_climbing_mejor_mejora(europa[4])
print("------------------------------------")

#Deimos
deimos = deimos()
print("Hill Climbing mejor-mejora: ")
hill_climbing_mejor_mejora(deimos[0])
print("------------------------------------")
hill_climbing_mejor_mejora(deimos[1])
print("------------------------------------")
hill_climbing_mejor_mejora(deimos[2])
print("------------------------------------")
hill_climbing_mejor_mejora(deimos[3])
print("------------------------------------")
hill_climbing_mejor_mejora(deimos[4])
print("------------------------------------")
