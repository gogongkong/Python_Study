'''
https://www.acmicpc.net/problem/1260
'''

from collections import deque

n, m, start = map(int, input().split())

datas = [[] for _ in range(n+1)]
result_bfs = []
for _ in range(m):
    a, b = map(int, input().split())
    datas[a].append(b)
    datas[b].append(a)

def bfs(start, datas):
    queue = deque()
    queue.append(start)
    visited = [False] * (n+1)
    visited[start] = True
    print(start,end=' ')
    while queue:
        now = queue.popleft()
        
        for next in datas[now]:
            if visited[next] == False:
                visited[next] = True
                queue.append(next)
                print(next, end=' ')

visited_dfs = [False] * (n+1)
def dfs(start, datas, visited_dfs):
    visited_dfs[start] = True
    print(start,end=' ')
    
    for next in datas[start]:
        if visited_dfs[next] == False:
            visited_dfs[next] == True
            dfs(next, datas,visited_dfs)
    
dfs(start, datas, visited_dfs)
print('\n')
bfs(start, datas)
        