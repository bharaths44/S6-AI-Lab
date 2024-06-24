from itertools import permutations

def calculate_route_distance(route, distance_matrix):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities):
        total_distance += distance_matrix[route[i]][route[(i + 1) % num_cities]]
    return total_distance

def tsp_brute_force(distance_matrix):
    num_cities = len(distance_matrix)
    all_routes = permutations(range(num_cities))
    min_distance = float('inf')
    best_route = None

    for route in all_routes:
        current_distance = calculate_route_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, min_distance = tsp_brute_force(distance_matrix)
print(f"Best route: {best_route}")
print(f"Minimum distance: {min_distance}")