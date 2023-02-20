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


