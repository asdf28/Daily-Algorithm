import sys


def solution():
    N = int(sys.stdin.readline().rstrip())
    arr = []

    for i in range(N):
        arr.append(int(sys.stdin.readline().rstrip()))

    arr.sort(reverse=True)

    for e in arr:
        print(e)


if __name__ == "__main__":
    solution()