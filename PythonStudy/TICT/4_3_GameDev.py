import sys

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int,sys.stdin.readline().split())
pos_x, pos_y, d = map(int, sys.stdin.readline().split())
gameMap = []
for i in range(N):
    gameMap.append(list(map(int, sys.stdin.readline().split())))

cnt = 1
while True:
    move = False

    for i in range(4):
        d -= 1
        if d < 0:
            d = 3

        nx = pos_x + dx[d]
        ny = pos_y + dy[d]

        if nx < 0 or nx >= N or ny < 0 or ny >= M or gameMap[nx][ny] == 1:
            continue
        cnt += 1
        gameMap[pos_x][pos_y] = 1

        pos_x = nx
        pos_y = ny

        move = True
        break

    if move is True:
        continue

    nx = pos_x - dx[d]
    ny = pos_x - dy[d]

    if nx < 0 or nx >= N or ny < 0 or ny >= M or gameMap[nx][ny] == 1:
        break

    pos_x = nx
    pos_y = ny

print(cnt)
