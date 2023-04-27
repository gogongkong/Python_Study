# https://www.acmicpc.net/problem/1158

from collections import deque
n, k = map(int, input().split())

queue = deque()
result = []
for i in range(1,n+1):
    queue.append(i)

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print(result)