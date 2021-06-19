import sys

while True:
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    li.sort()

    if li[2] == 0:
        break

    if li[2]**2 == li[0]**2 + li[1]**2:
        print("right")

    else:
        print("wrong")
