import sys

arr = list(map(int,sys.stdin.readline().rstrip()))

front = 0
back = 0

for i in arr[0:len(arr)//2]:
    front += i

for i in arr[len(arr)//2:]:
    back += i

if front == back:
    print("LUCKY")
else:
    print("READY")