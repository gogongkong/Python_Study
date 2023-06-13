'''
https://www.acmicpc.net/problem/7562
'''

from collections import deque

def bfs(x,y,targetx,targety,data):
    q = deque()
    q.append((x,y))
    dx = [2, 2, 1, 1, -2, -2, -1, -1]
    dy = [1, -1, 2, -2, 1, -1, 2, -2]

    while q:
        x, y = q.popleft()
        if targetx == x and targety == y:
            return data[targetx][targety]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                q.append((nx,ny))

tc = int(input())
result = []
for _ in range(tc):
    l = int(input())
    x, y = map(int, input().split())
    targetx, targety = map(int, input().split())
    data = [[0] * l for _ in range(l)]
    
    result.append(bfs(x,y,targetx,targety,data))
    
print(result)
