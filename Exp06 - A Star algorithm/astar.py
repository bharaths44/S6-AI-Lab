from collections import deque

def get_neighbors(node, adjacency_list):
    return adjacency_list[node]

def h(node):
    H = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H[node]

def a_star_algorithm(start_node, stop_node, adjacency_list):
    open_list = set([start_node])
    closed_list = set([])

    g = {}
    g[start_node] = 0

    parents = {}
    parents[start_node] = start_node

    while len(open_list) > 0:
        current_node = None

        for node in open_list:
            if current_node == None or g[node] + h(node) < g[current_node] + h(current_node):
                current_node = node

        if current_node == None:
            print('Path does not exist!')
            return None, float('inf')

        if current_node == stop_node:
            reconst_path = []

            while parents[current_node] != current_node:
                reconst_path.append(current_node)
                current_node = parents[current_node]

            reconst_path.append(start_node)
            reconst_path.reverse()

            total_cost = g[stop_node]
            return reconst_path, total_cost

        for (neighbor, weight) in get_neighbors(current_node, adjacency_list):
            if neighbor not in open_list and neighbor not in closed_list:
                open_list.add(neighbor)
                parents[neighbor] = current_node
                g[neighbor] = g[current_node] + weight
            else:
                if g[neighbor] > g[current_node] + weight:
                    g[neighbor] = g[current_node] + weight
                    parents[neighbor] = current_node

                    if neighbor in closed_list:
                        closed_list.remove(neighbor)
                        open_list.add(neighbor)

        open_list.remove(current_node)
        closed_list.add(current_node)

    print('Path does not exist!')
    return None, float('inf')

def main():
    adjacency_list = {
        'A': [('B', 2), ('E', 3)],
        'B': [('C', 1),('G', 9),('A',2)],
        'C': [('B',1)],
        'E': [('D', 6),('A',3)],
        'D': [('G', 1),('E',6)],
    }
    path, total_cost = a_star_algorithm('A', 'G', adjacency_list)
    print('Path found:', path)
    print('Total cost:', total_cost)

if __name__ == "__main__":
    main()