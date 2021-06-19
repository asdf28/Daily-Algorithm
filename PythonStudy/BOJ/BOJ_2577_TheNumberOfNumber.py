import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())

num = A * B * C
li = [0] * 10

while True:
    res = num % 10
    li[res] += 1

    if num < 10:
        break
    num //= 10

for i in range(10):
    print(li[i])

#best code
# a = int(input())
# b = int(input())
# c = int(input())
#
# d = list(map(int, (str(a * b * c))))
#
# for i in range(10):
#     print(d.count(i))
