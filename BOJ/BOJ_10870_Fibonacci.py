import sys


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)


N = int(sys.stdin.readline().rstrip())

print(fib(N))
