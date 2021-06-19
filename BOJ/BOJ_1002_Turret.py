import sys
import math

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r1 + r2 > dist > (max(r1, r2) - min(r1, r2)):
        print(2)
    elif r1 + r2 == dist or (max(r1, r2) - min(r1, r2)) == dist:
        print(1)
    else:
        print(0)
