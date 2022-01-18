#Uses python3

import sys

def reach(adj_list, visited, u, v):
    visited[u] = True
    for vertex in adj_list[u]:
        if not visited[vertex]:
            reach(adj_list, visited, vertex, v)


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = [] #connected
    adj_list = [[]for i in range(n_vertices + 1)]
    for i in range(n_edges):
        edges.append(tuple(map(int, input().split())))
    for (a,b) in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    u, v = map(int, input().split())
    #Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise
    visited = [False] * (n_vertices+1)
    reach(adj_list, visited, u, v)
    if visited[v] == True:
        print(1)
    else:
        print(0)

