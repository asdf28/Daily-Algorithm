import sys

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_team(parent, x, y):
    a = find_parent(x)
    b = find_parent(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, sys.stdin.readline().split())

parent = [0] * (N+1)

print(parent)
for i in range(N+1):
    parent[i] = i

for i in range(M):
    cal, x, y = map(int, sys.stdin.readline().split())

    if cal == 0:
        union_team(parent, x, y)
        continue

    if find_parent(x) == find_parent(y):
        print("YES")
    else:
        print("NO")
