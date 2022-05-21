import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]


def bfs(x, y):
    queue = deque()

    queue.append((x, y))
    while True:
        if len(queue) == 0:
            break

        x, y = queue.pop()

        arr[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if arr[nx][ny] == 0:
                queue.append((nx, ny))

        # if x < n-1 and arr[x+1][y] == 0:
        #     queue.append((x+1, y))
        # if y < m-1 and arr[x][y+1] == 0:
        #     queue.append((x, y+1))


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())

    arr = []

    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip())))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)
