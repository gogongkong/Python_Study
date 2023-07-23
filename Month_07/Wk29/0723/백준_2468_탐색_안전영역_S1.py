'''
https://www.acmicpc.net/problem/2468
'''

from collections import deque
import copy

# 2차원 배열의 행과 열을 입력(정사각형 구조)
n = int(input())

data = []
# 지도 입력
for _ in range(n):
    data.append(list(map(int, input().split())))

def bfs(x, y, height,data):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x,y))
    data[x][y] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > height:
                data[nx][ny] = -1
                queue.append((nx, ny))
    return 1

max_height = max(max(data))
answer = []
for height in range(max_height):
    copy_data = copy.deepcopy(data)
    result = 0
    for x in range(n):
        for y in range(n):
            if copy_data[x][y] > height:
                result += bfs(x, y, height, copy_data)
    answer.append(result)

print(max(answer))


