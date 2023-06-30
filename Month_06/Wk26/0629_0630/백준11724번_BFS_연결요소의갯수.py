'''
https://www.acmicpc.net/problem/11724
'''

from collections import deque

# 정점 N, 간선 M 입력
n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (n+1)

def bfs(x,visited, data):
    queue = deque()
    queue.append(x)
    visited[x] = True
    while queue:
        now = queue.popleft()
        for next in data[now]:
            if visited[next] == True:
                continue
            else:
                visited[next] = True
                queue.append(next)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        if not data[i]:
            count +=1
            visited[i] = True
        else:
            bfs(i, visited, data)
            count +=1

print(count)

