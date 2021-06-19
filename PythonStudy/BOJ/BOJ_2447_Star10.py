import sys

N = int(sys.stdin.readline().rstrip())


def star10(i, j, k):
    if (i // k) % 3 == 1 and (j // k) % 3 == 1:
        print(" ", end="")
    elif k == 1:
        print("*", end="")
    else:
        star10(i, j, k // 3)


for i in range(N):
    for j in range(N):
        star10(i, j, N)
    print("")
