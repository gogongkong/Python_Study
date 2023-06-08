'''
https://www.acmicpc.net/problem/2468
'''
from collections import deque
import copy
n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


height = max(max(data)) # 최대 물 높이 (= 이이상 올라가면 전부 물에 잠긴다는 의미)
result = [] # 결과를 담을 리스트
count = 0
def bfs(x,y,h,data):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= n or data[nx][ny] - h <= 0:
                continue
            elif data[nx][ny] != 0:
                data[nx][ny] = 0
                queue.append((nx,ny))
    return True

for h in range(height):
    data_copy = copy.deepcopy(data)
    #count = 0
    for i in range(n):
        for j in range(n):
            if bfs(i,j,h,data_copy):
                count += 1
    
    result.append(count)

print(result)
