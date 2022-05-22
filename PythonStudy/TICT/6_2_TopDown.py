import sys

if __name__ == "__main__":
    arr = []

    n = int(sys.stdin.readline().rstrip())

    for i in range(n):
        arr.append(sys.stdin.readline().rstrip())

    arr.sort(reverse=True)

    print(arr)