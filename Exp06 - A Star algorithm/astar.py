from collections import deque

def get_neighbors(v, adjacency_list):
    return adjacency_list[v]

def h(n):
    H = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H[n]

def a_star_algorithm(start_node, stop_node, adjacency_list):
      # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
    open_list = set([start_node])
    closed_list = set([])

    g = {}
    g[start_node] = 0

    parents = {}
    parents[start_node] = start_node

    while len(open_list) > 0:
        n = None

        for v in open_list:
            if n == None or g[v] + h(v) < g[n] + h(n):
                n = v

        if n == None:
            print('Path does not exist!')
            return None, float('inf')

        if n == stop_node:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start_node)
            reconst_path.reverse()

     
            total_cost = g[stop_node]
           
            return reconst_path, total_cost

        for (m, weight) in get_neighbors(n, adjacency_list):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)

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


# https://www.mygreatlearning.com/blog/a-search-algorithm-in-artificial-intelligence/