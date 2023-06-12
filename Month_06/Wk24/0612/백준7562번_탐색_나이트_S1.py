'''
https://www.acmicpc.net/problem/7562
'''

from collections import deque

def bfs(x,y,targetx, targety, data):
    # 나이트가 이동 가능한 8가지 경우의 수
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        if x == targetx and y == targety:
            return data[targetx][targety]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                queue.append((nx,ny))

tc = int(input())
result = []
for _ in range(tc):
    l = int(input())
    data = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    targetx, targety = map(int, input().split())
    result.append(bfs(x, y, targetx, targety, data))

print(result)
