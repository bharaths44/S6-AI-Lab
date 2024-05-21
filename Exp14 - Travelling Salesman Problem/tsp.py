import random
import math

def initial_solution(n, start_city):
    """Create an initial solution."""
    route = [start_city]
    unvisited_cities = list(range(n))
    unvisited_cities.remove(start_city)
    
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distances[route[-1]][city])
        route.append(nearest_city)
        unvisited_cities.remove(nearest_city)
    
    return route

def total_distance(route):
    """Calculate the total distance of the route."""
    total = 0
    for i in range(len(route) - 1):
        total += distances[route[i]][route[i + 1]]
    total += distances[route[-1]][route[0]]  # Return to starting city
    return total

def improve_solution(route):
    """Improve the solution by swapping two cities if it results in a shorter route."""
    improved = False
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route.copy()  # Create a copy of the original route
            new_route[i], new_route[j] = new_route[j], new_route[i]  # Swap cities
            new_distance = total_distance(new_route)
            if new_distance < total_distance(route):
                route = new_route  
                improved = True
    return route, improved

def find_shortest_route(n, start_city):
    """Find the shortest route by repeatedly improving the current route."""
    current_route = initial_solution(n, start_city)
    improved = True
    while improved:
        current_route, improved = improve_solution(current_route)
    
    return current_route

def main():
    """Main function to run the program."""
    global distances
    n = 4
    distances = [
        [math.inf, 10, 15, 20],
        [10, math.inf, 35, 25],
        [15, 35, math.inf, 30],
        [20, 25, 30, math.inf]
    ]
    start_city = 0

    best_route = find_shortest_route(n, start_city)
    best_distance = total_distance(best_route)
    best_route.append(start_city)
    print("Best Route:", [chr(city + 65) for city in best_route])  # Convert city indices back to letters
    print("Total Distance:", best_distance)

if __name__ == "__main__":
    main()