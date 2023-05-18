import copy
from greedy import costo, europa_greedy, titan_greedy, deimos_greedy

def tabu_search(data, max_tabu_size, max_iterations):
    # Initialize the best solution as the current one
    best_solution = copy.deepcopy(data)
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
    print("costo final: ", best_cost)
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
    best_cost = float('inf')
    best_neighbor = None
    for neighbor in neighbors:
        cost = costo(neighbor)
        if cost < best_cost:
            best_cost = cost
            best_neighbor = neighbor
    return best_neighbor, best_cost

#Titan
titan = titan_greedy()
print("Tabu Search: ")
tabu_search(titan,10,100)
print("------------------------------------")
tabu_search(titan,10,100)
print("------------------------------------")
tabu_search(titan,10,100)
print("------------------------------------")
tabu_search(titan,10,100)
print("------------------------------------")
tabu_search(titan,10,100)
print("------------------------------------")

#Europa
europa = europa_greedy()
print("Tabu Search: ")
tabu_search(europa, 10, 50)
print("------------------------------------")
tabu_search(europa, 10, 50)
print("------------------------------------")
tabu_search(europa, 10, 50)
print("------------------------------------")
tabu_search(europa, 10, 50)
print("------------------------------------")
tabu_search(europa, 10, 50)
print("------------------------------------")

#Deimos
deimos = deimos_greedy()
print("Tabu Search: ")
tabu_search(deimos, 10, 10)
print("------------------------------------")
tabu_search(deimos, 10, 10)
print("------------------------------------")
tabu_search(deimos, 10, 10)
print("------------------------------------")
tabu_search(deimos, 10, 10)
print("------------------------------------")
tabu_search(deimos, 10, 10)
print("------------------------------------")



