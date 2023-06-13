'''
https://www.acmicpc.net/problem/2583
'''

from collections import deque

m, n, k = map(int, input().split())
data = [[0] * n for _ in range(m)]

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            data[y][x] = 1

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 1
    data[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == 0:
                data[nx][ny] = 1
                queue.append((nx,ny))
                count += 1
    return count

result = []
for x in range(m):
    for y in range(n):
        if data[x][y] == 0:
            result.append(bfs(x,y))

print(result.sort())

