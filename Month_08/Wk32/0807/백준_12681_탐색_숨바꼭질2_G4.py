'''
https://www.acmicpc.net/problem/12851
'''

from collections import deque

MAX_value = 100000
n, k = map(int, input().split())

dp = [0] * (MAX_value+1)

queue = deque()
queue.append(n)
count = 0
route = 0
while queue:
    now = queue.popleft()

    if now == k:
        route = dp[now]
        count +=1
        continue
    
    for next in (now +1, now -1, now *2):
        if 0 <= next <= MAX_value and (dp[next] == 0 or dp[next] == dp[now] +1):
            dp[next] = dp[now] +1
            queue.append(next)

print(route)
print(count)