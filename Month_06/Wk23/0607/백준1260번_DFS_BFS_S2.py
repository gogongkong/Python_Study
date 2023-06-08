'''
https://www.acmicpc.net/problem/1260

아래 입력에 맞춰 DFS, BFS로 수행해보자

예제 입력 1 
4 5 1
1 2
1 3
1 4
2 4
3 4
예제 출력 1 
1 2 4 3
1 2 3 4
예제 입력 2 
5 5 3
5 4
5 2
1 2
3 4
3 1
예제 출력 2 
3 1 2 5 4
3 1 4 2 5
예제 입력 3 
1000 1 1000
999 1000
예제 출력 3 
1000 999
1000 999

'''
from collections import deque
import sys
input = sys.stdin.readline

# 노드 n, 간선 m, 시작노드 start
n, m, start = map(int, input().split())
data = [[] for _ in range(n+1)] # 간선의 정보를 담을 리스트
# 간선의 정보 입력, 양방향 연결, 노드 오름차순 정렬
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

for i in range(len(data)):
    data[i].sort()

# 방문 정보와 방문 순서를 담을 리스트 초기화
visited = [False] * (n+1)
result_dfs = [start]
result_bfs = [start]

def dfs(start, data, visited):
    visited[start] = True
    
    for next in data[start]:
        if not visited[next]:
            visited[next] = True
            result_dfs.append(next)
            dfs(next, data, visited)
            
    return result_dfs

def bfs(start, data, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        for next in data[now]:
            if not visited[next]:
                visited[next] = True
                result_bfs.append(next)
                queue.append(next)
    
    return result_bfs

dfs(start, data, visited)

for i in result_dfs:
    print(i,end=' ')
print()

visited = [False] * (n+1)

bfs(start, data, visited)

for i in result_bfs:
    print(i,end=' ')
print()
