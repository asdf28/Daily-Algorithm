import sys
import heapq


def dijkstra():
    q = []
    cnt_num = 0
    cnt_dst = 0

    heapq.heappush(q, (0, C))
    while q:
        d, n = heapq.heappop(q)
        if sp[n] < d:
            continue
        cnt_num += 1
        cnt_dst = max(cnt_dst, d)
        for e in graph[n]:
            if sp[e[0]] > d + e[1]:
                heapq.heappush(q, (d + e[1], e[0]))
                sp[e[0]] = d + e[1]
    print(cnt_num-1, cnt_dst)

    return


if __name__ == "__main__":
    N, M, C = map(int, sys.stdin.readline().split())

    sp = [int(1e9)] * (N+1)

    graph = [[] for i in range(N+1)]
    for x in range(M):
        src, dst, distance = map(int, sys.stdin.readline().split())

        graph[src].append((dst, distance))

    dijkstra()












