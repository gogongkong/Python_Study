'''
https://www.acmicpc.net/problem/16493
'''

n, m = map(int, input().split())

dp = [[0] * (n+1) for _ in range(m+1)]

date = [0]
chap = [0]

for _ in range(m):
    a, b = map(int, input().split())
    date.append(a)
    chap.append(b)

for i in range(1, m+1):
    for j in range(1,n+1):
        if date[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - date[i]] + chap[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])