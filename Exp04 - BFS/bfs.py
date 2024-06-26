from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, "\t")

        for i in range(len(graph[vertex])):
            if graph[vertex][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    # Initialize an empty adjacency matrix
    graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Take input for each edge
    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        graph[u][v] = 1
        graph[v][u] = 1  # Assuming undirected graph

    # Take input for the starting vertex
    start_vertex = int(input("Enter the starting vertex for BFS: "))

    # Perform BFS
    bfs(graph, start_vertex)

if __name__ == "__main__":
    main()