'''
https://www.acmicpc.net/problem/12851
'''

from  collections import deque

n, k = map(int, input().split())

# 이동가능 방법 n+1, n-1, 2 * n 3가지

MAX_dist = 10 ** 5

distance = [0] * (MAX_dist+1)


queue = deque()
queue.append(n)
min_route = 0
min_count = 0

while queue:
    now = queue.popleft()

    if now == k:
        min_route = distance[now]
        min_count += 1
        continue
    else:
        for next in (now -1, now +1, now *2):
            if 0 <= next <= MAX_dist and (
                distance[next] == 0 or distance[next] == distance[now]+1
            ):
                distance[next] = distance[now] +1
                queue.append(next)
print(min_route)
print(min_count)