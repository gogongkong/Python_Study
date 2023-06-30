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

def dfs(start):
    visited[start] = True
    
    # if not data[start]:
    #     return True

    for next in data[start]:
        if not visited[next]:
            dfs(next)
    

count = 0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)