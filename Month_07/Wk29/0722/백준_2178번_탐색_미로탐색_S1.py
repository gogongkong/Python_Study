'''
https://www.acmicpc.net/problem/2178
'''

from collections import deque

n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input())))

def BFS(n, m,data):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx, ny))
    
BFS(n, m, data)
print(data[n-1][m-1])