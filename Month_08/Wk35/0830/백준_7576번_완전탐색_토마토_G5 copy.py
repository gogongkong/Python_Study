'''
https://www.acmicpc.net/problem/7576
'''

from collections import deque

m, n = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * (m) for _ in range(n)]
queue = deque()
for x in range(n):
    for y in range(m):
        if data[x][y] == 1:
            queue.append([x,y])

dx, dy = [-1,1,0,0], [0,0,-1,1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                queue.append([nx, ny])

bfs()

for x in range(n):
    for y in range(m):
        if data[x][y] == 0:
            print(-1)
            exit(0)

print(max(max(data))-1)

