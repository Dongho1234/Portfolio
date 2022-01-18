#Uses python3

import sys

def dfs(graph, vertex, visited, postorder):
    global ctr
    visited[vertex] = True
    for i in graph[vertex]:
        if not visited[i]:
            dfs(graph, i, visited, postorder)
    postorder[vertex] = ctr
    ctr += 1


def toposort(n, edges, visited, postorder):

    for i in range(1, n+1):
        if not visited[i]:
            dfs(edges, i, visited, postorder)
    postorder = list(enumerate(postorder[1:], start= 1))
    postorder.sort(key=lambda  x:x[1], reverse=True)
    return postorder

if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = [[] for i in range(n_vertices+1)] #sink
    for i in range(n_edges):
        a, b = map(int, input().split())
        edges[a].append(b)
    visited = [False] * (n_vertices + 1)
    postorder = [0] * (n_vertices + 1)
    ctr = 1
    ans_order = toposort(n_vertices, edges, visited, postorder)
    for i, post in ans_order:
        print(i, end=' ')
