'''
https://www.acmicpc.net/problem/11724
'''

# 정점 N, 간선 M 입력
n, m = map(int, input().split())
data = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False] * (n+1)

def dfs(x):
    visited[x] = True
    for next in data[x]:
        if visited[next] == False:
            dfs(next)

count = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
