import sys

N = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))

li = set()
flg = False
cnt = 0

for i in range(2, 1000):
    flg = False
    for j in range(2, i):
        if i % j == 0:
            flg = True
            break
    if not flg:
        li.add(i)

for i in range(len(num)):
    if num[i] in li:
        cnt += 1

print(cnt)
