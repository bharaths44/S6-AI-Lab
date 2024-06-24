graph = {'A': [('B', 1), ('C', 3)], 
         'B': [('A', 1), ('D', 2), ('E', 4)], 
         'C': [('A', 3), ('F', 5)], 
         'D': [('B', 2)], 
         'E': [('B', 4), ('F', 1)], 
         'F': [('C', 5), ('E', 1)]
         }


heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 5, 'E': 3, 'F': 0}
priority_queue=[(0,"A",["A"],0)]
cost={"A":0}


while priority_queue:
    priority_queue.sort(key=lambda x: x[0])
    priority,node,path,curr_cost=priority_queue.pop(0)

    if node=="F":
        final_path,final_cost=path,curr_cost

    for i,j in graph[node]:
        new_cost=curr_cost+j
        if i not in cost or new_cost<cost[i]:
            cost[i]=new_cost
            priority_queue.append((new_cost+heuristic[i],i,path+[i],new_cost))


print("->".join(final_path),final_cost,sep="\n")