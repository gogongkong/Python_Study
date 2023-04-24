'''
문제
N x M 크기의 직사각형 형태의 미로에 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 
현재 위치는 (1, 1)이고 미로의 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 
괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 
미로는 반드시 탈출할 수 있는 형태로 제시된다. 
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력
첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다. 
다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다. 
각각의 수들은 공백 없이붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.
출력
첫째 줄에 최소 이동 칸의 개수를 출력한다.

[입력 예시]
5 6
101010
111111
000001
111111
111111

[출력 예시]
10
'''
from collections import deque

n, m = map(int, input().split())

arr = []

for _ in range(n): # 맵 입력
    arr.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1] # 상 하 좌 우 방향을 담은 리스트

def bfs(x,y): # BFS 함수 작성
    queue = deque() # 큐 선언
    queue.append((x,y)) # 큐에 시작지점 삽입
    while queue: # 큐가 빌 때까지
        x, y = queue.popleft() # queue에서 첫 번째 원소 빼기
        for i in range(4):
            nx = x + dx[i] # 다음 이동할 위치
            ny = y + dy[i]
            # 맵 밖을 벗어나거나 벽인 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m or arr[nx][ny] == 0: 
                continue
            if arr[nx][ny] == 1: # 다음 위치가 올바른 위치인 경우
                arr[nx][ny] = arr[x][y] + 1 # 직전위치의 값 + 1
                queue.append((nx, ny)) # 다음위치를 큐에 삽입(다음 반복에서 현재위치로 사용)
    return arr[n-1][m-1] # 탈출구 위치의 값 리턴

print(bfs(0,0))
