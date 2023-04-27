'''
https://www.acmicpc.net/problem/11060
'''
from collections import deque

n = int(input())
queue = deque()
a = list(map(int, input().split()))
for i in a:
    queue.append(i)

count = 0
while queue:
    index = queue.popleft()
    n -= 1
    count += 1
    if n != 0 or index < n:
        for i in range(index):
            