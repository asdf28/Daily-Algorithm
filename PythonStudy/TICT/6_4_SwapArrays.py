import sys

N, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort()

index_a = 0
index_b = len(B) - 1

for i in range(K):
    if A[index_a] > B[index_b]:
        break
    A[index_a], B[index_b] = B[index_b], A[index_a]

    index_a += 1
    index_b -= 1

print(sum(A))


