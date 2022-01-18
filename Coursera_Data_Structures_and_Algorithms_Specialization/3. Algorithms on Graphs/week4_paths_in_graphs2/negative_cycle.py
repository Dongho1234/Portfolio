#Uses python3

import sys


def negative_cycle(n_vertices, edges):
    dist = [1000] * (n_vertices+1)
    #edge weights are integers of absolute value at most 10^3
    dist[1] = 0
    negative_weight = []
    for i in range(n_vertices):
        for a, b, w in edges:
            if dist[b] > dist[a] + w:
                dist[b] = dist[a] + w
                if i == n_vertices - 1:
                    negative_weight.append(b)
    if not negative_weight:
        return 0
    else:
        return 1


if __name__ == '__main__':
    n_vertices, n_edges =  map(int, input().split())
    edges = []
    for i in range(n_edges):
        a, b, w = map(int, input().split())
        # a = start, b = end, w = weight
        edges.append((a,b,w))
    negative_cycle(n_vertices, edges)
    print(negative_cycle(n_vertices,edges))
