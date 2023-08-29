'''
https://www.acmicpc.net/problem/5014
'''

from collections import deque

F, S, G, U, D = map(int, input().split())

dp = [0] * (F+1)
visited = [False] * (F+1)

def bfs(S):
    queue = deque([S])
    visited[S] = True
    dp[S] = 0

    while queue:
        now = queue.popleft()

        if now == G:
            return print(dp[now])

        for next in (now + U, now - D):
            if 0 < next <= F and visited[next] == False:
                visited[next] = True
                dp[next] = dp[now] + 1
                queue.append(next)
    if dp[S] == 0:
        return print(-1)
    

bfs(S)