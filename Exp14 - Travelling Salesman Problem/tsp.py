import random
import math

def calculate_distance(city1, city2):
    """Calculate the distance between two cities."""
    return distances[cities.index(city1)][cities.index(city2)]

def initial_solution(cities, start_city):
    """Create an initial solution."""
    route = [start_city]
    unvisited_cities = cities.copy()
    unvisited_cities.remove(start_city)
    
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: calculate_distance(route[-1], city))
        route.append(nearest_city)
        unvisited_cities.remove(nearest_city)
    
    return route

def total_distance(route):
    """Calculate the total distance of the route."""
    total = 0
    for i in range(len(route) - 1):
        total += calculate_distance(route[i], route[i + 1])
    total += calculate_distance(route[-1], route[0])  # Return to starting city
    return total

def improve_solution(route):
    """Improve the solution by swapping two cities if it results in a shorter route."""
    improved = False
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route[:i] + [route[j]] + route[i+1:j] + [route[i]] + route[j+1:]
            new_distance = total_distance(new_route)
            if new_distance < total_distance(route):
                route = new_route
                improved = True
    return route, improved

def find_shortest_route():
    """Find the shortest route by repeatedly improving the current route."""
    current_route = initial_solution(cities, start_city)
    improved = True
    while improved:
        current_route, improved = improve_solution(current_route)
    
    return current_route

def main():
    """Main function to run the program."""
    global cities, distances, start_city
    cities = ['A', 'B', 'C', 'D']
    distances = [
        [math.inf, 10, 15, 20],
        [10, math.inf, 35, 25],
        [15, 35, math.inf, 30],
        [20, 25, 30, math.inf]
    ]
    start_city = 'A'

    best_route = find_shortest_route()
    best_distance = total_distance(best_route)
    best_route.append(start_city)
    print("Best Route:", best_route)
    print("Total Distance:", best_distance)

if __name__ == "__main__":
    main()