'''
https://www.acmicpc.net/problem/1260
'''

from collections import deque

n, m, start = map(int, input().split())

data = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited_bfs = [False] * (n+1)
result_bfs = []

def bfs(start, data, result_bfs):
    queue = deque()
    queue.append(start)
    result_bfs.append(start)
    visited_bfs[start] = True
    for next in data[start]:
        if visited_bfs[next] == False:
            visited_bfs[next] = True
            result_bfs.append(next)
            queue.append(next)

bfs(start, data, result_bfs)

visited_dfs = [False] * (n+1)
result_dfs = []

def dfs(start, data, result_dfs):
    visited_dfs[start] = True
    result_dfs.append(start)
    for next in data[start]:
        if visited_dfs[next] == False:
            visited_dfs[next] = True
            dfs(next, data, result_dfs)

dfs(start, data, result_dfs)

print(result_bfs)
print(result_dfs)