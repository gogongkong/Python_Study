'''
https://www.acmicpc.net/problem/11724
'''

from collections import deque

n, m = map(int, input().split())

data = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (n+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()

        for next in data[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

count = 0

for i in range(1,n+1):
    if not data[i]:
        count += 1
        visited[i] = True
    else:
        if not visited[i]:
            bfs(i)
            count += 1

print(count)