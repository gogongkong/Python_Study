'''
https://www.acmicpc.net/problem/16234
'''
from collections import deque

N, L, R = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    temp = []
    queue.append((x,y))
    temp.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(data[nx][ny] - data[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    temp.append((nx,ny))
    return temp

result = 0
while True:
    visited = [[0] * (N+1) for _ in range(N+1)]
    check = 0
    for i in range(N):
        for k in range(N):
            if visited[i][k] == 0:
                visited[i][k] = 1
                country = bfs(i,k)

                if len(country) > 1:
                    check = 1
                    num = sum([data[x][y] for x,y in country]) // len(country)
                    for x,y in country:
                        data[x][y] = num
    if check == 0:
        break
    result += 1
print(result)
                    

    
