# python3
import itertools

#number of rooms and corridors connecting the rooms respectively.
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

adj = [[] for _ in range(n)]
clauses = []
position = range(1,n+1)

for i, j in edges:
    adj[i-1].append(j-1)
    adj[j-1].append(i-1)

def var_num(i, j):
    return n * i + j

def exactly_one_of(literals):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
# each node can only appear once in the path and
# every position in the path can only have one node

for i in range(n):
    exactly_one_of([var_num(i,j) for j in position])


for j in position:
    exactly_one_of([var_num(i, j) for i in range(n)])


for j in position[:-1]:
    for i, nodes in enumerate(adj):
        clauses.append([-var_num(i, j)] + [var_num(n, j+1) for n in nodes])


print(len(clauses), n * n)
for c in clauses:
    c.append(0)
    print(' '.join(map(str, c)))
