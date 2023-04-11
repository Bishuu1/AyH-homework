import copy
from itertools import combinations
import time


def print_colored_grid(grid):
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


def create_possibilities(values, no_of_other):
    possibilities = []

    for v in values:
        groups = len(v)
        no_empty = no_of_other-sum(v)-groups+1
        ones = [[1]*x for x in v]
        res = combinationss(no_empty, groups, ones)
        possibilities.append(res)

    return possibilities


def combinationss(n_empty, groups, ones):
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


def nonogramSolver(columnPossibilities, rowPossibilities, nonogram, inicio):
    indice = inicio
    columnsToCheck = copy.deepcopy(columnPossibilities)
    completo_una_vuelta = False
    while (nonogram[indice][0] != 0):
        indice += 1
        if indice >= len(nonogram):
            if completo_una_vuelta:
                break
            indice = 0
            completo_una_vuelta = True

        if indice == inicio and completo_una_vuelta:
            # print("el nonograma es while:", )
            # print_colored_grid(nonogram)
            return 1
    else:

        for j in range(len(rowPossibilities[indice])):  # recorremos las posibilidades para cada fila
            columnPossibilities = copy.deepcopy(columnsToCheck)

            nonogram[indice] = rowPossibilities[indice][j]  # asignamos la posibilidad a la fila correspondiente
            # recorremos las columnas para encontrar a cuales afectas y quitar las posilibidades que ya no son factibles
            for count, column in enumerate(columnPossibilities):
                if column == []:
                    break
                for posibility in reversed(column):
                    if posibility[indice] != nonogram[indice][count]:
                        column.remove(posibility)  # quitamos la posibilidad que no es factible
                if column == []:
                    break

                if count == len(nonogram[0]) - 1:
                    contador = sum(1 for elemento in columnPossibilities if isinstance(elemento, list) and elemento)
                    if contador >= len(nonogram[0]) and indice != len(nonogram[0]) - 1:
                        # llamamos recursivamente para ver si el nonograma esta completo
                        if nonogramSolver(columnPossibilities, rowPossibilities, nonogram, indice) == False:
                            break
                        else:
                            return 1
                    elif contador >= len(nonogram[0]) and indice == len(nonogram) - 1:
                        print("el nonograma es:")
                        print_colored_grid(nonogram)
                        return 1
        # deshacemos la asignación de la posibilidad a la fila correspondiente
        nonogram[indice] = [0] * len(nonogram[indice])
        return False


row_clues = [
    [4],
    [8],
    [10],
    [1, 1, 2, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 6, 1],
    [6],
    [2, 2],
    [4],
    [2]
]

col_clues = [
    [4],
    [2],
    [7],
    [3, 4],
    [7, 2],
    [7, 2],
    [3, 4],
    [7],
    [2],
    [4]
]
RP = create_possibilities(row_clues, 10)
CP = create_possibilities(col_clues, 10)

nonogram = [[0 for _ in range(10)] for _ in range(10)]

nonogramSolver(CP, RP, nonogram, 0)
# heuristic = []
# times = 1000
# for i in range(times):
#     t1_start = time.perf_counter()
#     nonogramSolver(CP, RP, nonogram, 2)
#     heuristic.append(time.perf_counter() - t1_start)
# print(sum(heuristic)/times)
#
# forward_checking = []
# for i in range(times):
#     t1_start = time.perf_counter()
#     nonogramSolver(CP, RP, nonogram, 0)
#     forward_checking.append(time.perf_counter() - t1_start)
# print(sum(forward_checking)/times)
