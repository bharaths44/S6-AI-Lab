def dfs(graph, start, visited=None):
    if visited is None:
        visited = [False] * len(graph)
    visited[start] = True
    print(start, "\t")

    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

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
    start_vertex = int(input("Enter the starting vertex for DFS: "))

    # Perform DFS
    dfs(graph, start_vertex)

if __name__ == "__main__":
    main()