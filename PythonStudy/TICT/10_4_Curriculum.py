import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for i in range(N+1)]
indegree = [0] * (N+1)
time = [0] * (N+1)
result = [0] * (N+1)
q = deque()

for i in range(1, N+1):
    data = list(map(int, sys.stdin.readline().split()))

    time[i] = data[0]
    result[i] = data[0]

    for j in data[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        print(i, result, time)
        result[i] = max(result[now] + time[i], result[i])
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

print(result)