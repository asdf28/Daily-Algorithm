import sys


def backtracking(depth, li, visited, answer):
    if depth == M:
        for e in answer:
            print(e, end=" ")
        print()
        return

    for i in range(N):
        if visited[i]:
            continue

        # visited[i] = True
        answer.append(li[i])
        backtracking(depth+1, li, visited, answer)
        # visited[i] = False
        answer.pop()



def solution():
    li = []
    tmp = set()
    visited = [False] * N
    answer = []

    li = list(map(int,sys.stdin.readline().split()))

    li.sort()
    #
    # for x in range(N):
    #     li.append(x+1)

    backtracking(0, li, visited, answer)


N, M = map(int, sys.stdin.readline().split())
solution()