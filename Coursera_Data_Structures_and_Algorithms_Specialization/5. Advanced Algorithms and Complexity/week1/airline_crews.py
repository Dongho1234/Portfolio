#python 3

from collections import deque


def network(n, m, bip):

    graph = [[0] * (n + m + 2) for _ in range(n + m + 2)]

    for i in range(1, n + 1):
        graph[0][i] = 1 #n_flight
        for j in range(m):
            #crew
            graph[i][n + 1 + j] = bip[i - 1][j]
    for k in range(n + 1, n + m + 1):
        #n_crew
        graph[k][-1] = 1
    return graph

def find_path(graph, path):
    visited = [False] * len(graph)
    visited[0] = True
    queue = deque([0])
    while queue:
        #source
        temp = queue.popleft()
        if temp == len(graph) - 1:
            #gives path
            return True
        for i in range(len(graph)):
            if not visited[i] and graph[temp][i] > 0:
                # Gf[temp][i] > 0 check if it has path to next edges
                queue.append(i)
                #next edges
                visited[i] = True
                path[i] = temp #save path from back
    return visited[len(graph)-1]


def MaxFlow(graph, n):
    maxflow = 0
    path = list(range(len(graph)))
    while find_path(graph, path):

        min_flow = float('inf')
        v = len(graph) - 1

        while v != 0:
            u = path[v]
            #[current][next path] in graph = gives capacity
            min_flow = min(min_flow, graph[u][v]) # u = temp
            #find min capacity in the path from backward
            v = u # ex) 2 -> 5, 1 -> 2

        # add flow in every edge of the path
        # make new residual graph
        v = len(graph) - 1
        while v != 0:
            u = path[v]
            graph[u][v] -= min_flow
            graph[v][u] += min_flow
            v = u
        maxflow += min_flow
    matches = [-1] * n
    for i in range(len(graph)):
        if graph[-1][i] ==  1:
            crew = i - n
            flight = graph[i].index(1)
            matches[flight-1] = crew
    return matches

if __name__ == '__main__':
    n_flights, n_crews = map(int, input().split())
    bipartite = [list(map(int, input().split())) for i in range(n_flights)]

    residual_graph = network(n_flights,n_crews, bipartite)
    max_flow = MaxFlow(residual_graph, n_flights)
    for i in max_flow:
        print(i, end=' ')

