import sys

list_x = []
list_y = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if x in list_x:
        list_x.remove(x)
    else:
        list_x.append(x)
    if y in list_y:
        list_y.remove(y)
    else:
        list_y.append(y)

print(list_x[0], list_y[0])