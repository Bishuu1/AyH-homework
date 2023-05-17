import copy
from greedy_estocastico import leer_archivo, greedy_estocastico, costo

def tabu_search(data, max_tabu_size, max_iterations):
    # Initialize the best solution as the current one
    print("helloS")
    best_solution = copy.deepcopy(data)
    print("hello")
    best_cost = costo(data)

    tabu_list = [best_solution]

    for _ in range(max_iterations):
        neighbors = get_neighbors(best_solution)

        best_neighbor, best_neighbor_cost = find_best_neighbor(neighbors)

        if best_neighbor_cost < best_cost and best_neighbor not in tabu_list:
            best_solution = copy.deepcopy(best_neighbor)
            best_cost = best_neighbor_cost


        tabu_list.append(best_neighbor)


        if len(tabu_list) > max_tabu_size:
            tabu_list.pop(0)

    return best_solution


def get_neighbors(data):
    neighbors = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            neighbor = copy.deepcopy(data)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def find_best_neighbor(neighbors):
    print("searching jeje", len(neighbors))
    best_cost = float('inf')
    best_neighbor = None
    for neighbor in neighbors:
        cost = costo(neighbor)
        if cost < best_cost:
            best_cost = cost
            best_neighbor = neighbor
    return best_neighbor, best_cost

def pruebas(sorted_data):
    array = ["prueba 1", "prueba 2"]
    pruebas = []
    for each in array:
        value = copy.deepcopy(sorted_data)
        pruebas.append(greedy_estocastico(value, each))
    return pruebas
print("1")
uavs = leer_archivo("t2_Deimos.txt")
print("2")
sorted_data = sorted(uavs, key=lambda x: x[1][1])
print("3")
estocastico = pruebas(sorted_data)
print("4")

print(tabu_search(estocastico[0],10,100))