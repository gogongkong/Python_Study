'''
https://www.acmicpc.net/problem/7576
'''

from collections import deque

m, n = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(n):
    for k in range(m):
        if data[i][k] == 1:
            queue.append([i, k])

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                queue.append([nx, ny])
    
bfs()

for x in range(n):
    for y in range(m):
        if data[x][y] == 0:
            print(-1)
            exit(0)
        result = max(result, data[x][y])

print(result-1)

