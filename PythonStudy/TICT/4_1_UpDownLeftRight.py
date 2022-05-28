import sys

N = int(sys.stdin.readline().rstrip())

plans = list(map(str,sys.stdin.readline().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direct = ['L', 'R', 'U', 'D']

pos_x = 0
pos_y = 0
#
for plan in plans:
    for i in range(4):
        if plan == direct[i]:
            nx = pos_x + dx[i]
            ny = pos_y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny > N:
                break

            pos_x, pos_y = nx, ny

print(pos_x + 1, pos_y + 1)