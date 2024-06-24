graph={}
vertices=int(input("Enter the number of vertices : "))
for i in range(vertices):
    vertex=input(f"Enter the vertex {i+1} : ")
    graph[vertex]=list(map(str,input(f"Enter neighbours of vertex {i+1} separated by space :  ").split()))
start_node=input("Enter the start node : ")
visited=set()
queue=[start_node]
while queue:
    node=queue.pop(0)
    print(node)
    if node not in visited:
        visited.add(node)
        for i in graph[node]:
            if i not in visited and i not in queue:
                queue.append(i)