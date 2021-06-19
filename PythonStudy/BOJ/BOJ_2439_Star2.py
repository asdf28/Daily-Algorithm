import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print("")

# better code
# x=int(input())
# for i in range(1,x+1):
#     print(' '*(x-i)+'*'*i)
#