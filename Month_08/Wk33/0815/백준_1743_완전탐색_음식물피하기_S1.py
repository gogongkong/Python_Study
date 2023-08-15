'''
https://www.acmicpc.net/problem/1743
'''

# 가장 큰 음식물만 피하라 == 그래프를 그렸을때 가장 많이 인접해있는 부분의 칸수

from collections import deque

n, m, k = map(int, input().split())

data =[[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

result = []
def bfs(data, x, y):
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1

    while queue:
        x, y = queue.popleft()
        data[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx <= n and 0 < ny <= m and data[nx][ny] == 1:
                data[nx][ny] = 0 
                count += 1
                queue.append((nx,ny))

    return count

for x in range(1, n+1):
    for y in range(1, m+1):
        if data[x][y] == 1:
            result.append(bfs(data,x,y))

print(max(result))