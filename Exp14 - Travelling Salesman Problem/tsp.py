import random
import math

# Step 2: Define the cities, distances, and starting city
cities = ['A', 'B', 'C', 'D']
distances = [
    [math.inf, 10, 15, 20],
    [10, math.inf, 35, 25],
    [15, 35, math.inf, 30],
    [20, 25, 30, math.inf],

]
start_city = 'A'

# Step 3: Create an initial solution
def initial_solution(cities, start_city):
    route = [start_city]
    unvisited_cities = cities.copy()
    unvisited_cities.remove(start_city)
    
    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distances[cities.index(route[-1])][cities.index(city)])
        route.append(nearest_city)
        unvisited_cities.remove(nearest_city)
    
    return route

# Step 4: Calculate the total distance of the route
def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distances[cities.index(route[i])][cities.index(route[i + 1])]
    total += distances[cities.index(route[-1])][cities.index(route[0])]  # Return to starting city
    return total

# Step 5: Improve the solution
def improve_solution(route):
    improved = False
    for i in range(len(route)):
        for j in range(i + 1, len(route)):
            new_route = route[:i] + [route[j]] + route[i+1:j] + [route[i]] + route[j+1:]
            new_distance = total_distance(new_route)
            if new_distance < total_distance(route):
                route = new_route
                improved = True
    return route, improved

# Step 6: Repeat steps 4 and 5 until a satisfactory solution is found
def find_shortest_route():
    current_route = initial_solution(cities, start_city)
    improved = True
    while improved:
        current_route, improved = improve_solution(current_route)
    
    return current_route

# Step 7: Return the best solution
best_route = find_shortest_route()
best_distance = total_distance(best_route)
best_route.append(start_city)
print("Best Route:", best_route)
print("Total Distance:", best_distance)

# Step 8: Stop
# https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/