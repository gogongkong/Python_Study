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

''' 2월 22일 공부 시작'''

# 음료수 얼려먹기 실전문제

# 얼음틀의 세로n 가로m 입력받기
n, m = map(int, input().split())

# 얼음틀의 형태 입력 받기
arr = []
for i in range(n):
    arr.append(list(map(int, input())))
def dfs(x, y):
    #틀을 벗어난 경우
    if x<=-1 or x>=n or y <=-1 or y>=m:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x+1, y)
        dfs(x,y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == False:
            dfs(i,j)
            result += 1
print(result)   

''' 실전문제 미로탈출 '''
from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    #큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 공간을 벗어난 경우
            if nx<=-1 or nx >=n or ny<=-1 or ny>=m:
                continue
            #벽인 경우 무시
            if arr[nx][ny] == 0:
                continue
            # 처음 방문하는 노드의 경우
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y]+1
                queue.append((nx,ny))
    return arr[n-1][m-1]
print(bfs(0,0))



''' 답안 없이 100% 자력으로 풀어보기 '''
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

            if nx <= -1 or nx>=n or ny <= -1 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] +1
                queue.append((nx,ny))
    return arr[n-1][m-1]

print(bfs(0,0))

''' DFS 메서드 정의'''
def dfs (graph, v, visited):
    visited[v] = True # 현재 노드 방문 처리
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, v, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

''' BFS '''

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(queue)구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9
bfs(graph, 1, visited)


''' 음료수 얼려 먹기 '''
n, m = map(int, input().split())

arr = []
for _ in range(n):
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
    return False

result =0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs(i,j)
            result +=1

print(result)

''' 미로 탈출 '''
from collections import deque
n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] +1
                queue.append((nx,ny))
    
    return arr[n-1],[m-1]

print(bfs(0,0))
    



''' 음료수 얼려 먹기 예제 자력으로 풀기 도전'''
# 얼음틀 만들기 - 얼음틀 크기 입력받기
n, m = map(int, input().split())

# 얼음틀 만들기 - 얼음틀 입력받기
arr = [] # 얼음틀을 입력받을 공백 리스트
for i in range(n):
    arr.append(list(map(int, input())))

# DFS 함수 만들기
def dfs(x,y):
    # 얼음틀을 벗어 날 때
    if x <=-1 or y <=-1 or x >= n or y >= m:
        return False
    # 음료수를 넣지 않은 칸 일때
    if arr[x][y] == 1:
        return False
    # 음료수 넣은 칸 일때
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# DFS 함수를 이용하여 문제 풀기
result = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y) == True:
            result += 1

print(result)

''' 미로 탈출 BFS 자력으로 풀어보기 '''
# queue 사용을 위한 deque 라이브러리 불러오기
from collections import deque

# 미로 크기 입력받기
n, m = map(int, input().split())

# 미로 입력받을 공백 리스트 생성 후 미로 입력 받기
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

# 상 하 좌 우를 구현할 리스트 생성
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수 작성
def bfs(x, y):
    queue = deque()
    ''' 오답 : queue = deque'''
    # queue에 x,y 좌표 삽입
    queue.append((x,y))

    while queue: # queue가 빈공간이 될 때 while문 탈출
        x, y = queue.popleft()
        ''' 오답 : queue.popleft()'''
        for i in range(4): # 기준 위치(x,y)에서 네방향으로 뻗어나가기
            nx = x+dx[i]
            ny = y+dy[i]

            # 미로의 크기를 벗어난 경우
            if nx <= -1 or ny <= -1 or nx >=n or ny >=m:
                continue
            # 벽인 경우 무시
            if arr[nx][ny] == 0:
                continue
            # 처음 방문한 노드
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] +1 # 방문한 노드에 +1 해서 표시 하기
                queue.append((nx, ny))
    # 최단거리 반환
    return arr[n-1][m-1]

print(bfs(0, 0))

''' 그리디 문제 : 거스름 돈 '''
n = 1260
coin_type = [500, 100, 50, 10]
count = 0

for coin in coin_type:
    count += n//coin
    n %= coin

print(count)

''' 그리디 문제 : 큰 수의 법칙'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse= True)
first = data[0]
sec = data[1]
result = 0
while True:
    if m == 0:
        break
    for i in range(k):
        result += first
        m -= 1
    result += sec
    m-=1

print(result)

''' 숫자 카드 게임 '''
n, m = map(int, input().split())
result = []
for i in range(n):
    data = map(int, input().split())
    result.append(min(data))

print(max(result))

''' 그리디 문제 1이 될 때 까지 '''
n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k != 0:
        cnt += n%k
        n -= n%k
    elif n % k == 0:
        n = n/k
        cnt += 1

print(cnt)


''' 상 하 좌 우 '''

n = int(input())
x, y = 1, 1
steps = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']

for step in steps:
    for i in range(len(direction)):
        if step == direction[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    if nx<1 or ny <1 or nx >n or ny>n:
        continue
    
    x, y = nx, ny

print(x,y)


''' 시각 '''
n = int(input())
cnt = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1
print(cnt)

''' 왕실의 나이트 '''
move = input()
row = int(move[1])
colum = int(ord(move[0])) - int(ord('a')) +1

steps = [(2,1), (-2,1), (2,-1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]
cnt = 0
for step in steps:
    next_row = row + step[0]
    next_colum = colum + step[1]
    # if next_row >= 1 and next_row <=8 and next_colum >= 1 and next_colum <=8:
    #     cnt+=1
    if next_row < 1 or next_row > 8 or next_colum < 1 or next_colum >8:
        continue
    else:
        cnt+=1
print(cnt)

''' DFS '''
n, m = map(int, input().split())
arr =[]
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >=n or y <=-1 or y>=m:
        return False
    if arr[x][y] == 1:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False
cnt = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y) == True:
            cnt +=1
print(cnt)


''' BFS '''
from collections import deque
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx <=-1 or ny <= -1 or nx >= n or ny >= m:
                    continue
                if arr[nx][ny] == 0:
                    continue
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    queue.append((nx,ny))
    return arr[n-1][m-1]
print(bfs(0,0))

''' 게임 개발 예제 '''

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
d = [[0] * m for _ in range(n)]
d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북0 동1 남2 서3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction =3

turn_time = 0
count = 1
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if arr[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        turn_time = 0
        count +=1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time =0
print(count)


''' DFS '''
n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or y <= -1 or x >=n or y >= m:
        return False
    if arr[x][y] == 1:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x, y-1)
        return True
    return False

result = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y) == True:
            result += 1
print(result)

''' 미로 탈출 '''
from collections import deque
n, m = map(int, input().split())
arr= []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))

    return arr[n - 1][m - 1]

print(bfs(0,0))


''' 
정렬
데이터를 특정한 기준에 따라서 순서대로 나열하는 것
선택정렬, 삽입정렬, 퀵정렬, 계수정렬을 많이 사용함
기본 정렬 라이브러리도 존재
'''

num = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(num)
# 오름차순 정렬
num.sort()
print(num)
# 내림차순 정렬
num.sort(reverse= True)
print(num)

'''
선택정렬
가장 작은것을 맨 앞에 있는 데이터와 바꾸고 그 다음 작은 데이터를 선택해 두번째 데이터와 바꾸는것
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i] # 스와프

print(arr)

''' 스와프 소스 코드 '''
array = [3, 5]
array[0], array[1] = array[1], array[0]
print(array)

'''
삽입정렬 소스코드
두번째 데이터부터 시작 - 첫번째 데이터는 그 자체로 정렬이 되어 있다고 생각하기 때문에
'''
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(arr)):
    for j in range(i, 0, -1): # i부터 하나씩 감소하는 방식
        if arr[j] > arr[j-1]: # 한 칸씩 왼쪽으로 이동
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(arr)


'''
퀵 정렬
'''

arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left  = start +1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수햄
    quick_sort(arr, start, right -1)
    quick_sort(arr, right +1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)


'''파이썬의 장점을 살린 퀵 정렬 소스 코드'''
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0] # 피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x<= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))


'''
계수정렬
특정 조건에 부합할 때만 사용가능하지만 매우 빠른 정렬 알고리즘
단, 가장 큰 데이터와 작은 데이터의 차이가 크면 안됨
모든 벙위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문
'''

# 계수정렬 예제
# 모든 원소의 값이 0보다 크다고 가정
arr = [ 7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트를 선언(모든 값은 0으로 초기화)
count = [0] * (max(arr)+1)

for i in range(len(arr)):
    count[arr[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end= ' ') # 띄어쓰기를 구분으로 등장한 횟수 만큼 인덱스 출력

'''
파이썬 기본 정렬 라이브러리
sorted() 함수를 제공 - 병합정렬 방식을 사용함 퀵정렬보다는 느리지만 최악의 경우에도 O(NlogN)을 보장
'''

# sorted 소스코드
arr = [7,5,9,0,3,1,6,2,4,8]
result = sorted(arr)
print(result)

'''
리스트 변수가 하나 있을때 내부원소를 바로 정렬가능
리스트 객체의 내장함수인 sort() 사용 - 별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬
'''
arr = [7,5,9,0,3,1,6,2,4,8]
arr.sort()
print(arr)

'''
sorted(), sort()를 이용할 때 key 매개변수를 입력 받을 수 있음
key값으로는 하나의 함수가 들어가야 하며 이는 정렬의 기준이 됨
EX : 리스트의 데이터가 튜플로 구성되어 있을 때 각 데이터의 두번째 원소를 기준으로 설정하는 경우
'''

arr = [('바나나', 2), ('사과', 5), ('당근',3)]
def setting(data):
    return data[1]

#result = sorted(arr, key= setting)
#print(result)
arr.sort(key= setting)
print(arr)

