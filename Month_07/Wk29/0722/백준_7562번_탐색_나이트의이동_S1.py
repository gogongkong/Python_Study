'''
https://www.acmicpc.net/problem/7562
'''

from collections import deque
tc = int(input())

direction = [(2,1), (-2,1), (2,-1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]

result = []

def bfs(x,y,a,b,data):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            if x == a and y == b:
                return data[x][y]
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny))

for _ in range(tc):
    n = int(input())

    data = [[0] *(n) for _ in range(n)]

    x, y = map(int, input().split())
    a, b = map(int, input().split())
    result.append(bfs(x,y,a,b,data))

for i in result:
    print(i)

