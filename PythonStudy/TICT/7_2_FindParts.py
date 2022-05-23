import sys

N = int(sys.stdin.readline().rstrip())
stock = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().split()))


def binarySearch(left, right):
    if left > right:
        return None

    mid = (left + right) // 2

    if stock[mid] == thing:
        return mid

    if stock[mid] < thing:
        return binarySearch(mid + 1, right)
    else:
        return binarySearch(left, mid - 1)


stock.sort()

for thing in find:
    if binarySearch(0, len(stock) - 1) is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
