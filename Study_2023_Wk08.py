'''
DFS 깊이 우선 탐색
인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식
인접 리스트 : 리스트로 그래프의 연결관예를 표현하는 방식
'''

# 인접행렬 - 2차원 배열에 노드가 연결된 형태를 기록하는 방식
INF = 999999999 # 무한의 비용 선언
# 2차원 리스트를 이용해 인접 행렬 표현

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

# 인접 리스트 - 모든 노드에 연결된 노드에 대한 정보를 연결하여 저장
# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5))

print(graph)

'''
DFS는 스택 자료구조를 이용
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다.
방문하지 않은 인접 노드가 없으면 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
'''

# DFS 메서드 정의
def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)


'''
BFS 너비 우선 탐색 - 가까운 노드부터 탐색
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리.
3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복한다.
'''

# BFS 예제
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 BFS 함수 호출
bfs(graph, 1, visited)


''' 예제 5-10 151p 음료수 얼려 먹기'''
# N, M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당노드 방문 처리
        graph[x][y] = 1
        # 상 하 좌 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result +=1

print(result)

'''
DFS / BFS
DFS = 한쪽만 파다 돌아오는거
BFS = 뻗어나가는거
'''

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
arr = []
d = [[0] * m for _ in range(m)]
d[x][y] = 1
for i in range(n):
    arr.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3

# 북0 동1 남2 서3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        cnt +=1
        turn_time = 0
        continue
    else:
        turn_time +=1
    if turn_time ==4:
        nx = x-d[nx][ny]
        ny = y-d[nx][ny]
        if d[nx][ny] == 0 and arr[nx][ny] == 0:
            x, y = nx, ny
            cnt+=1
            turn_time =0
        else:
            break

print(cnt)

''' 왕실의 나이트 '''
data = input()
row = int(data[1])
colum = int(ord(data[0])) - int(ord('a')) +1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt = 0
for step in steps:
    step_row = row+step[0]
    step_colum = colum+step[1]
    if step_row >= 1 and step_row <= 8 and step_colum >= 1 and step_colum <= 8:
        cnt += 1

print(cnt)


''' 음료수 얼려 먹기 예제 '''

# 얼음틀의 세로길이N, 가로길이M
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우에는 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if arr[x][y] == 0:
            # 해당노드 방문처리
            arr[x][y] = 1
            # 상 하 좌 우
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

# 모든 위치에 대해 음료수 채우기
result = 0
for x in range(n):
    for y in range(m):
        # 현재 위치에 대해 dfs 수행
        if dfs(x, y) == True:
            result += 1

print(result) # 결과 출력
n, m = map(int, input().split())

''' 미로 탈출 152p'''
from collections import deque
# N,M 크기의 직사각형 입력 받기
n, m = map(int, input().split())

# 미로 입력받기
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

# 이동할 네 방향 정의 ( 상 하 좌 우 )
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스 구현
def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx <0 or ny <0 or nx >=n or ny >=m:
                continue
            # 벽인 경우 무시
            if arr[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return arr[n-1][m-1]

# BFS를 수행한 결과 출력 
print(bfs(0,0))


''' 음료수 얼려먹기 다시 풀어보기 '''
# 얼음틀 가로 세로 n, m 입력 받기
n, m = map(int, input().split())
# 얼음틀 입력
arr =[]
for i in range(n):
    arr.append(list(map(int, input())))

# dfs 함수 만들기
def dfs(x, y):
    if x <=-1 or x >= n or y<=-1 or y>= m:
        return False
    
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x -1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1
print(result)



n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x, y):
    if x <=-1 or x>=n or y<=-1 or y>=m:
        return False

    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)


''' 그리디 거스름돈 다시 풀어보기 '''
n = 1260 
coin_type = [500, 100, 50, 10]
count = 0
for coin in coin_type:
    count += n // coin
    n %= coin

print(count)

''' 큰수의 법칙 '''
n, m , k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
sec = data[1]

result = 0
while True:
    if m != 0:
        for i in range(k):
            result += first
            m -= 1

        result += sec
        m -= 1 
    elif m == 0:
        break

print(result)

''' dfs 연습문제 '''

n , m = map(int, input().split())

arr= []
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

''' 미로탈출 '''
from collections import deque
n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))
    return arr[n-1][m-1]
print(bfs(0,0))