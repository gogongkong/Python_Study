'''
https://www.acmicpc.net/problem/16234
'''
from collections import deque
import sys

input = sys.stdin.readline
N, L, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    answer = []
    answer.append((x,y))
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(data[nx][ny] - data[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    answer.append((nx,ny))
    return answer

Flag = 0
while True:
    visited = [[0] * (N+1) for _ in range(N+1)]
    check = 0

    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                visited[x][y] = 1
                country = bfs(x,y)

                if len(country) > 1:
                    check = 1
                    num = sum(data[i][j] for i, j in country) // len(country)
                    for i, j in country:
                        data[i][j] = num
    
    if check == 0:
        break
    Flag += 1
print(Flag)