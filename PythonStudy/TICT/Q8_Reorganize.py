import sys

arr = list(map(str, sys.stdin.readline().rstrip()))
charArr = []
num = 0

for i in arr:
    if i.isdigit():
        num += int(i)
    else:
        charArr.append(i)

charArr.sort()

for tmp in charArr:
    print(tmp, end="")
print(num)