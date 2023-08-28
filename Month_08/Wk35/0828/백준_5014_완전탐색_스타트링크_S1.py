'''
https://www.acmicpc.net/problem/5014
'''

# 현위치 S
# 목표위치 G
# 가장 높은 층 F

from collections import deque

F, S, G, U, D = map(int, input().split())

stair = [0 for _ in range(F+1)]

visited = [False] * (F+1)

def bfs(start, visited, U, D, F, G, stair):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        now = queue.popleft()
        if now == G:
            return stair[G]
        for next in (now + U, now - D):
            if 0 < next <= F and visited[next] == False:
                stair[next] = stair[now] + 1
                visited[next] = True
                queue.append(next)
    
    if stair[G] == 0:
        return "use the stairs"

print(bfs(S, visited, U, D, F, G, stair))