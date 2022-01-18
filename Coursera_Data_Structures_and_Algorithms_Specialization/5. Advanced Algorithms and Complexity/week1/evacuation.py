#python 3

from collections import deque

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


def MaxFlow(graph):
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

    return maxflow

if __name__ == '__main__':
    n_city, n_edges = map(int, input().split())
    residual_graph = [[0] * n_city for i in range(n_city)]
    for _ in range(n_edges):
        u, v, capacity = map(int, input().split())
        residual_graph[u - 1][v - 1] += capacity
    max_flow = MaxFlow(residual_graph)
    print(max_flow)

