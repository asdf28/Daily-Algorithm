import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

li = set()
flg = False

if M == 1:
    M += 1
for i in range(M, N+1):
    flg = False
    for j in range(2, i):
        if i % j == 0:
            flg = True
            break
    if not flg:
        li.add(i)

if len(li) == 0:
    print(-1)

else:
    print(sum(li))
    print(min(li))