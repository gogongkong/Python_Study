'''
https://www.acmicpc.net/problem/1697
'''

from  collections import deque

n, k = map(int, input().split())

# 이동가능 방법 n+1, n-1, 2 * n 3가지

MAX_dist = 10 ** 5

distance = [0] * (MAX_dist+1)

def bfs(n, k, distance):
    queue = deque()
    queue.append(n)
    

    while queue:
        now = queue.popleft()

        if now == k:
            print(distance[now])
            break
        else:
            for next in (now -1, now +1, now *2):
                if 0 <= next <= MAX_dist and distance[next] == 0:
                    distance[next] = distance[now] +1
                    queue.append(next)

bfs(n,k,distance)
