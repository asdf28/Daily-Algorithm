import sys

x, y, w, h = map(int,sys.stdin.readline().rstrip().split())

min = x

if y < min:
    min = y

if w - x < min:
    min = w - x

if h - y < min:
    min = h - y

print(min)
