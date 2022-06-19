import sys


def backTracking(depth, prev, li, answer):
    if depth == M:
        print(answer)
        return

    for i in range(N):
        if li[i] < prev:
            continue

        backTracking(depth+1, li[i], li, answer + str(li[i]) + " ")


N, M = map(int,sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

tmp = set()

for e in li:
    if e in tmp:
        N -= 1

    tmp.add(e)

li = list(tmp)

li.sort()

backTracking(0, 0, li, "")