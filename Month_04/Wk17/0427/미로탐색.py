from collections import deque

n, m = map(int, input().split())

data = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue: # 큐가 빌때 까지 반복
        x, y = queue.popleft()
        for i in range(4): # 상 하 좌 우 반복
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= m or data[nx][ny] == 0:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny))
    return data[n-1][m-1]

print(bfs(0,0))