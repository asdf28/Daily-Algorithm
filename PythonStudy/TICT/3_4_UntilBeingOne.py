import sys

def solution(N,K):
    cnt = 0
    while N > 1:
        if N % K == 0:
            N //= K
        else:
            N -= 1
        cnt += 1
    return cnt


N, K = map(int,sys.stdin.readline().split())
print(solution(N,K))