import sys

direction = ['LU', 'LD', 'RU', 'RD', 'UL', 'UR', 'DL', 'DR']
dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

pos_y, pos_x = map(str, sys.stdin.readline().rstrip())

pos_y = ord(pos_y) - 97
pos_x = int(pos_x) - 1

print(pos_x, pos_y)
cnt = 0
for i in range(8):
    nx = pos_x + dx[i]
    ny = pos_y + dy[i]

    if nx >= 8 or nx < 0 or ny >= 8 or ny < 0:
        continue
    print(nx, ny)
    cnt += 1

print(cnt)
