import sys

T = int(sys.stdin.readline().rstrip())

ap = [[1] * 14 for _ in range(16)]

for i in range(1, 16):
    for j in range(1, 14):
        ap[i][j] = ap[i-1][j] + ap[i][j-1]

for t in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    print(ap[k+1][n-1])
