import sys

li = list()

for i in range(9):
    li.append(int(sys.stdin.readline().rstrip()))

print(max(li), li.index(max(li))+1)
