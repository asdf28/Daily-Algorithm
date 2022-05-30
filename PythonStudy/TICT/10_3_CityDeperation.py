import sys


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, sys.stdin.readline().split())

parent = [0] * (N+1)
graph = []

for i in range(1, N+1):
    parent[i] = i

for i in range(M):
    a, b, upkeep = map(int, sys.stdin.readline().split())
    graph.append((upkeep, a, b))

graph.sort(key=lambda tmp: tmp[0])

cnt = 0
max_fee = 0
for i in graph:
    if find_parent(i[1]) != find_parent(i[2]):
        union_parent(i[1], i[2])
        cnt += i[0]
        max_fee = max(max_fee, i[0])
print(cnt - max_fee)