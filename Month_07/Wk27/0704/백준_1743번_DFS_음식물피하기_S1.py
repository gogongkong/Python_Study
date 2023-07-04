'''
https://www.acmicpc.net/problem/1743
'''

from collections import deque

n, m, k = map(int, input().split())

data = [[0] * (m + 1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    data[x][y] = 2
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx <= n and 0 < ny <= m and data[nx][ny] == 1:
                data[nx][ny] = 2
                count += 1
                queue.append((nx,ny))
       
    return count

result = []
for x in range(1, n+1):
    for y in range(1, m+1):
        if data[x][y]:
            result.append(bfs(x,y))

print(max(result))
