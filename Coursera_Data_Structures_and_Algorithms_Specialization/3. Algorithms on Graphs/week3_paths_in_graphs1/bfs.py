#Uses python3

from collections import deque



def breadth_first_search(n, adj, start, end):
    dist = [-1]  * (n+1)
    queue = deque()
    queue.append(start)

    #bfs to get
    dist[start] = 0
    while queue:
        now = queue.popleft()
        for vertex in adj[now]:
            if dist[vertex] == -1: #check distance == infinity

                queue.append(vertex)
                dist[vertex] = dist[now] + 1

    return dist[end]


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    adj_list = [[] for i in range(n_vertices+1)]
    for i in range(n_edges):
        a,b = map(int, input().split())
        #undirected graph
        adj_list[a].append(b)
        adj_list[b].append(a)
    u, v = map(int, input().split())
    distance = breadth_first_search(n_vertices, adj_list, u, v)
    if distance == -1:
        print(-1)
    else:
        print(distance)

