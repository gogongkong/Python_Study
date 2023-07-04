'''
https://www.acmicpc.net/problem/1697
'''

from collections import deque

n, k = map(int, input().split())
MAX = 10 **5
dist = [0] * (MAX + 1)

def bfs(n, k):
    queue = deque()
    queue.append(n)
    
    while queue:
        x = queue.popleft()

        if x == k:
            print(dist[x])
            break
        else:
            for nx in (x -1, x +1, x *2):
                if 0 <= nx <= MAX and not dist[nx]:
                    dist[nx] = dist[x]+1
                    queue.append(nx)


bfs(n,k)
