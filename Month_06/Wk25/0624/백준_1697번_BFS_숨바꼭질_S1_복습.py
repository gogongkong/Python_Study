'''
https://www.acmicpc.net/problem/1697
'''

'''
수빈이의 위치 N, 동생의 위치 K 입력

걷기 = N+1 혹은 N-1, 순간이동 = 2 * N

동생을 찾는 가장 빠른 시간을 출력
'''

from collections import deque

n, k = map(int, input().split())

num = 10 ** 5

dp = [0] * (num+1)

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        now = queue.popleft()
        if now == k:
            print(dp[now])
            break
        for next in (now +1, now -1, now *2):
            if 0<= next <= num and not dp[next]:
                dp[next] = dp[now] + 1
                queue.append(next)
bfs()