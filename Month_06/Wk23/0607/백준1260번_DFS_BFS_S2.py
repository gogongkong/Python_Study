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

n, m, start = map(int, input().split()) # 노드 : n / 간선 : m / 시작점 : start
data = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
visited = [False] * (n+1)

result_bfs = [start]
result_dfs = [start]

def dfs(start, data, visited):
    visited[start] = True
    for i in data[start]:
        if not visited[i]:
            visited[i] = True
            result_dfs.append(i)
            dfs(i, data, visited)
    return result_dfs

for i in dfs(start, data, visited):
    print(i, end=' ')
print()

visited = [False] * (n+1)

def bfs(start, data, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        for i in data[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result_bfs.append(i)

    print(result_bfs)

bfs(start, data, visited)