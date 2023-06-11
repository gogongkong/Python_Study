'''
https://www.acmicpc.net/problem/2468
'''

from collections import deque

n = int(input())
data = []

data = [list(map(int, input().split())) for _ in range(n)]

max_height = max(max(data))

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(x, y, value, visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
    
result = 0
for i in range(max_height):
    visited = [[0] *n for _ in range(n)]
    count = 0

    for x in range(n):
        for y in range(n):
            if data[x][y] > i and visited[x][y] == 0:
                bfs(x, y, i, visited)
                count += 1 

    if result < count:
        result = count

print(result)