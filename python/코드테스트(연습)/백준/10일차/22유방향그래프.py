n = 7
graph = [[0] * n for _ in range(n)]
graph_list = [[],[],[],[],[],[],[]]
for _ in range(6):
    v1,v2 = map(int, input().split())
    graph[v1][v2] = 1
    
    graph_list[v1].append(v2)
    
print(graph)
print(graph_list)

"""
6 5
1 2
2 5
5 1
3 4
4 6
"""