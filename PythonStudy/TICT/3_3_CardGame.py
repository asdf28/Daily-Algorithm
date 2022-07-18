import sys

def solution():
    N, M = map(int,sys.stdin.readline().split())

    answer = 0
    for i in range(N):
        tmp = list(map(int,sys.stdin.readline().split()))
        min_val = min(tmp)
        answer = max(answer, min_val)

    return answer


print(solution())