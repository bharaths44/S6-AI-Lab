from collections import defaultdict

# Step 2: Read a graph from the user in the form of a dictionary and list
def addEdge(adjList, u, v):
    adjList[u].append(v)
    adjList[v].append(u)

# Step 3: Initialize a list 'visited'
visited = []

# Step 4: Create a function 'dfs' and perform the following operations:
def dfs(graph, vertex):
    # Step 4.1: Mark the current vertex as visited
    visited.append(vertex)
    print(vertex,"\t")

    # Step 4.2: Recursively visit all adjacent vertices that have not been visited yet
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor)

# Take input for the number of edges
num_edges = int(input("Enter the number of edges: "))

# Initialize an empty adjacency list
graph = defaultdict(list)

# Take input for each edge
for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    addEdge(graph, u, v)

# Take input for the starting vertex
start_vertex = int(input("Enter the starting vertex for DFS: "))

# Perform DFS
dfs(graph, start_vertex)

# Input :
# 0, 1
# 0, 2
# 1, 3
# 1, 4
# 2, 4