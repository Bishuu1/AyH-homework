import copy
from itertools import combinations
import time
import os

# Official
row_clues = [[4],[8],[10],[1, 1, 2, 1, 1],[1, 1, 2, 1, 1],[1, 6, 1],[6],[2, 2],[4],[2]]
col_clues = [[4],[2],[7],[3, 4],[7, 2],[7, 2],[3, 4],[7],[2],[4]]

# Car
cp = [[4],[10],[10],[9],[1,4],[1,4],[9],[1,5],[2,2],[3]]
rp = [[7],[3,1],[3,1],[3,1],[3,1],[9],[10],[8,1],[10],[2,2]]

# amongus
ccp = [[2],[4],[1,1],[1,2]]
rrp = [[3],[2],[4],[1,1]]


def print_colored_grid(grid): #Funcion para imprimir el nonograma
    for row in grid:
        for cell in row:
            if cell == 1:
                # green background for cells with value 1
                print("\033[42m  \033[m", end="")
            elif cell == -1:
                # red background for cells with value -1
                print("\033[41m  \033[m", end="")
            else:
                # black background for cells with value 0
                print("\033[40m  \033[m", end="")
        print()
    #print(grid[2])


def create_possibilities(values, no_of_other): #Funcion para crear las posibilidades de cada fila o columna
    possibilities = []
    for v in values:
        groups = len(v)
        no_empty = no_of_other-sum(v)-groups+1
        ones = [[1]*x for x in v]
        res = combinationss(no_empty, groups, ones)
        possibilities.append(res)
    return possibilities

def combinationss(n_empty, groups, ones): #Funcion para crear las combinaciones de las posibilidades dada las pistas
    res_opts = []
    for p in combinations(range(groups+n_empty), groups):
        selected = [-1]*(groups+n_empty)
        ones_idx = 0
        for val in p:
            selected[val] = ones_idx
            ones_idx += 1
        res_opt = [ones[val]+[-1] if val > -1 else [-1] for val in selected]
        res_opt = [item for sublist in res_opt for item in sublist][:-1]
        res_opts.append(res_opt)
    return res_opts



def nonogramSolver(columnPossibilities, rowPossibilities, nonogram, inicio, inicio_real, printt = True): #Funcion para resolver el nonograma
    indice = inicio #indice para recorrer las filas
    columnsToCheck = copy.deepcopy(columnPossibilities) #copiamos las columnas para no modificarlas
    completo_una_vuelta = False #variable para saber si ya recorrimos una vez el nonograma
    while (nonogram[indice][0] != 0): #mientras la fila no este vacia
        indice += 1
        if indice >= len(nonogram): #si ya recorrimos todas las filas
            if completo_una_vuelta: #si ya recorrimos una vez el nonograma
                break
            indice = 0 #volvemos a empezar
            completo_una_vuelta = True #indicamos que ya recorrimos una vez el nonograma

        if indice == inicio and completo_una_vuelta: #si ya recorrimos una vez el nonograma y estamos en la fila que empezamos
            if printt == True:
                print_colored_grid(nonogram)
            return 1
    else:

        for j in range(len(rowPossibilities[indice])):  # recorremos las posibilidades para cada fila
            columnPossibilities = copy.deepcopy(columnsToCheck) #copiamos las columnas para no modificarlas
            nonogram[indice] = rowPossibilities[indice][j] #asignamos la posibilidad a la fila correspondiente
            # print_colored_grid(nonogram)#imprimimos el nonograma dinamicamente, activar para ver el proceso
            
            ## recorremos las columnas para encontrar a cuales afectas y quitar las posilibidades que ya no son factibles
            for count, column in enumerate(columnPossibilities): #recorremos las columnas
                if column == []: #doble comprobacion para que no se rompa el codigo
                    break
                for posibility in reversed(column): #recorremos las posibilidades de la columna
                    if posibility[indice] != nonogram[indice][count]: #si la posibilidad no es factible
                        column.remove(posibility)  # quitamos la posibilidad que no es factible
                if column == []: #si la columna esta vacia, no hay posibilidades
                    break

                if count == len(nonogram[0]) - 1: #si ya recorrimos todas las columnas
                    contador = sum(1 for elemento in columnPossibilities if isinstance(elemento, list) and elemento) #contamos cuantas columnas tienen posibilidades y no quedaron con posibilidades vacias
                    if contador >= len(nonogram[0]) and indice != inicio_real - 1: #si todas las columnas tienen posibilidades y no estamos en la ultima fila
                        if nonogramSolver(columnPossibilities, rowPossibilities, nonogram, indice, inicio_real) == False: #llamamos recursivamente a la funcion para resolver el nonograma
                            break #si no se pudo resolver, rompemos el ciclo
                        else: #si se pudo resolver
                            return 1 
                    # elif contador >= len(nonogram[0]) and indice == len(nonogram) - 1:
                    elif contador >= len(nonogram[0]) and indice == inicio_real - 1: #si todas las columnas tienen posibilidades y estamos en la fila anterior a la que empezamos
                        if printt == True:
                            print_colored_grid(nonogram) #imprimimos el nonograma
                        return 1 
        nonogram[indice] = [0] * len(nonogram[indice])
        return False


def main(row_clues, col_clues, inicio):
    l = len(row_clues)
    RP = create_possibilities(row_clues, l)
    CP = create_possibilities(col_clues, l)

    nonogram = [[0 for _ in range(10)] for _ in range(10)]
    nonogramSolver(CP, RP, nonogram, inicio, inicio)
    times = 1000

    forward_checking = []
    for i in range(times):
        t1_start = time.perf_counter()
        nonogramSolver(CP, RP, nonogram, 0, 0, False)
        forward_checking.append(time.perf_counter() - t1_start)
    print("el tiempo en promedio luego de", times, "ejecuciones sin heuristica fue:", sum(forward_checking)/times)

    heuristic = []
    
    for i in range(times):
        t1_start = time.perf_counter()
        nonogramSolver(CP, RP, nonogram, 2, 2, False)
        heuristic.append(time.perf_counter() - t1_start)
    print("el tiempo en promedio luego de", times, "ejecuciones con heuristica fue:", sum(heuristic)/times)

main(row_clues, col_clues, 0)

