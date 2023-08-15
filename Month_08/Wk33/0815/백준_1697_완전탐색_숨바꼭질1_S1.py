'''
https://www.acmicpc.net/problem/1697
'''

# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.

from collections import deque

n, k = map(int, input().split())
MAX_value = 100000
data = [0] * (MAX_value + 1)

queue = deque()
queue.append(n)

while queue:
    now = queue.popleft()

    if next == k:
        break

    for next in (now -1, now +1, now *2):
        if 0 <= next < MAX_value and data[next] == 0:
            data[next] = data[now] + 1
            queue.append(next)

print(data[k])