from collections import defaultdict, deque

# Step 2: Read a graph from the user in the form of a dictionary and list
def addEdge(adjList, u, v):
    adjList[u].append(v)
    adjList[v].append(u)

# Step 3: Initialize two lists 'visited' and 'queue'
visited = []
queue = deque()

# Step 4: Create a function 'bfs' and perform the following operations:
def bfs(graph, start):
    # Step 4.1: Start by putting any one of the graph’s vertices at the back of the queue.
    queue.append(start)
    visited.append(start)
    
    # Step 4.4: Continue from Step 4.2 to Step 4.3, until the queue is empty.
    while queue:
        # Step 4.2: Now take the front item of the queue and add it to the visited list.
        vertex = queue.popleft()
        print(vertex,"\t")
        
        # Step 4.3: Create a list of that vertex’s adjacent nodes. Add those which are not within the visited list to the rear of the queue.
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Take input for the number of edges
num_edges = int(input("Enter the number of edges: "))

# Initialize an empty adjacency list
graph = defaultdict(list)

# Take input for each edge
for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    addEdge(graph, u, v)

# Take input for the starting vertex
start_vertex = int(input("Enter the starting vertex for BFS: "))

# Perform BFS
bfs(graph, start_vertex)
