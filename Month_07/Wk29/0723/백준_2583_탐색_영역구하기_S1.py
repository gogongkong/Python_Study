'''
https://www.acmicpc.net/problem/2583
'''

from collections import deque

m, n, k = map(int, input().split())

data = [[0] * (n) for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            data[j][i] = 1


def bfs(x, y, data):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x,y))
    data[x][y] = 1
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == 0:
                data[nx][ny] = 1
                count += 1
                queue.append((nx, ny))
    return count

result = []
for x in range(m):
    for y in range(n):
        if data[x][y] == 0:
            result.append(bfs(x, y, data))

print(len(result))
result.sort()
print(*result)    

