'''
https://www.acmicpc.net/problem/2468
'''


'''
풀이 접근
똑같은 크기의 0과 1로 이루어진 방문여부를 위한 리스트 생성
지도상 가장 높은 높이를 구하여 0부터 최대 높이까지 반복하여 해당 높이보다 큰 지점을 방문여부 파악
== 지도는 비교용으로 사용 실제 bfs에서 카운트하며 확인하는건 방문여부 리스트
'''
from collections import deque

n = int(input()) # 맵의 크기 입력

data = [list(map(int,input().split())) for _ in range(n)]  # 맵 입력

max_height = max(max(data)) # 맵의 최대 높이 입력


def bfs(x,y,value,visited): # BFS 함수 작성
    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1] 

    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1 # 현재 위치 방문처리
    while queue:
        x, y = queue.popleft() # 큐에서 x, y 값 빼내기
        for i in range(4): # 상 하 좌 우 전부 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > value and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))


result = 0
for value in range(max_height):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if data[x][y] > value and visited[x][y] == 0:
                bfs(x,y,value,visited)
                count += 1
    if result < count:
        result = count

print(result)
