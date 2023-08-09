'''
https://www.acmicpc.net/problem/17484
'''

n, m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (m)
for i in range(m):
    dp[i] = data[0][i]

for i in range(1, n):
    for k in range(m):
        if 0 < k < m-2:
            dp[i][k] = min(dp[i-1][k-1], dp[i-1][k+1]) + dp[i][k]
        elif k == m-1:
            dp[i][k] = dp[i-1][k-1] + dp[i][k]
        elif k == 0:
            dp[i][k] = dp[i-1][k+1] + dp[i][k]


print(min(dp[n-1]))