import sys


def solution(cur, pick, ans, visited):
    if pick == 0:
        print(ans)
        return

    for i in range(N):
        if visited[i]:
            continue

        visited[i] = True
        ans.append(i+1)
        solution(i, pick-1, ans, visited)
        ans.pop()
        visited[i] = False


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    solution(0, M, [], [False] * N)
































