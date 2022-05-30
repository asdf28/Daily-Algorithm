import heapq
import sys


def dijkstra():
    q = []
    stpath = [1e9] * (N+1)

    heapq.heappush(q, (0, C))
    stpath[C] = 0

    for i in range(N):
        if len(q) == 0:
            break

        dst, cur = heapq.heappop(q)

        if stpath[cur] < dst:
            continue

        for con in graph[cur]:
            cost = stpath[cur] + con[0]

            if cost < stpath[con[1]]:
                stpath[con[1]] = cost
                heapq.heappush(q, (cost, con[1]))

    city = 0
    distance = 0
    for i in range(1, N+1):
        if stpath[i] != 1e9:
            city += 1
            distance = max(distance, stpath[i])

    print(city - 1, distance)


N, M, C = map(int, sys.stdin.readline().split())

graph = [[] for x in range(N + 1)]
for x in range(M):
    X, Y, Z = map(int, sys.stdin.readline().split())

    graph[X].append((Z, Y))

dijkstra()
