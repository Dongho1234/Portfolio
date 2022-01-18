#Uses python3
import sys
import math

def minimum_distance(n, edges):
    #sort by distance
    sorted_edges = sorted(edges, key=lambda x:x[2])

    connection = []
    for j in range(n):
        connection.append(j)

    min_dist = 0
    for i in sorted_edges:
        print(connection, connection[i[1]], connection[i[0]])
        if connection[i[0]] != connection[i[1]]:
            min_dist += i[2]
            connection = list(map(lambda x: connection[i[0]] if x == connection[i[1]] else x,connection))

    return min_dist


if __name__ == '__main__':
    n_vertices = int(input())
    points = []
    for i in range(n_vertices):
        a,b = map(int, input().split())
        points.append((a,b))
    edges = []
    for i in range(n_vertices):
        #strat
        (x0, y0) = points[i]
        for j in range(i+1, n_vertices):
            (x,y) = points[j] #end
            distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
            edges.append((i,j, distance))
    print("{0:.9f}".format(minimum_distance(n_vertices,edges)))
