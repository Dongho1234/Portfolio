#Uses python3

import sys
import queue
import heapq

def distance(adj, cost,ctr, s, t):
    dist = [ctr + 1 ] * len(adj)
    dist[s] = 0
    h = list(zip(dist,range(len(dist))))
    heapq.heapify(h)
    while len(h) > 0:
        u = heapq.heappop(h)
        for i, j in enumerate(adj[u[1]]):
            if dist[j] > u[0] + cost[u[1]][i]:
                dist[j] = u[0] + cost[u[1]][i]
                heapq.heappush(h,(dist[j], j))
    if dist[t] == ctr +1 :
        return -1

    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # two vertices 𝑢 and 𝑣 , w (weights)
    data = data[3 * m:]
    ctr = 0
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        ctr += w
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, ctr,s, t))
