#use Sieve of Eratosthenes
import math
import sys

N = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
li = [True]*1001
li[0] = False
li[1] = False

for i in range(2, int(math.sqrt(1000))+1):
    j = 2
    while i*j <= 1000:
        li[i*j] = False
        j += 1

for i in range(N):
    if li[num[i]]:
        cnt += 1

print(cnt)


#
# li = set()
# flg = False
# cnt = 0
#
# for i in range(2, 1000):
#     flg = False
#     for j in range(2, i):
#         if i % j == 0:
#             flg = True
#             break
#     if not flg:
#         li.add(i)
#
# for i in range(len(num)):
#     if num[i] in li:
#         cnt += 1
#
# print(cnt)
