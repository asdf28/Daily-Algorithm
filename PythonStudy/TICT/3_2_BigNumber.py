import sys


def solution(N, M, K):
    arr.sort()

    max_num = arr[-1]
    max_prev = arr[-2]

    unit = (max_num * K) + max_prev
    cnt = 0

    cnt += unit * (M//(K+1))

    M %= (K+1)

    if M > 0:
        cnt += max_num * M

    return cnt


if __name__ == "__main__":
    N, M, K = map(int, sys.stdin.readline().split())

    arr = list(map(int, sys.stdin.readline().split()))

    print(solution(N, M, K))