import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = []
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    queue = deque()

    queue.append(((0, 0), 0))

    while True:
        if len(queue) == 0:
            break

        pos, dist = queue.popleft()
        visited[pos[0]][pos[1]] = True

        if pos[0] == n-1 and pos[1] == m-1:
            return dist + 1

        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue

            if maze[nx][ny] == 1 and visited[nx][ny] == False:
                queue.append(((nx, ny), dist + 1))


if __name__ == "__main__":
    for x in range(n):
        maze.append(list(map(int,sys.stdin.readline().rstrip())))

    print(bfs())
