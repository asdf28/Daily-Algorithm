# import heapq
# import sys
# from pprint import pprint
#
#
# def main():
#     N, M = map(int, sys.stdin.readline().split())
#     graph = [[1e9] * (N+1) for i in range(N+1)]
#
#     for i in range(M):
#         src, dst = map(int, sys.stdin.readline().split())
#
#         graph[src][dst] = 1
#         graph[dst][src] = 1
#
#     X, K = map(int, sys.stdin.readline().split())
#
#     for i in range(N + 1):
#         graph[i][i] = 0
#
#     for k in range(1, N + 1):
#         for i in range(1, N + 1):
#             for j in range(1, N + 1):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
#     print(graph[1][K] + graph[K][X])
#
#
# if __name__ == "__main__":
#     main()


import sys


def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    if graph[1][K] == int(1e9) or graph[K][x] == int(1e9):
        print(-1)
        return

    print(graph[1][K] + graph[k][X])
    return


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    graph = [[int(1e9)] * (N+1) for x in range(N+1)]

    for x in range(1, N+1):
        graph[x][x] = 0

    for x in range(M):
        s, d = map(int, sys.stdin.readline().split())
        graph[s][d] = 1
        graph[d][s] = 1
    X, K = map(int, sys.stdin.readline().split())

    floyd()