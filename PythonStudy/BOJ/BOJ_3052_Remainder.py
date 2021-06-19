import sys

RemainderList = set()
for i in range(10):
    RemainderList.add(int(sys.stdin.readline().rstrip()) % 42)

print(len(RemainderList))
