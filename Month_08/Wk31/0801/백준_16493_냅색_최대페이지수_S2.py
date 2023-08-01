'''
https://www.acmicpc.net/problem/16493
'''

n, m = map(int, input().split())

date = [0]
chapter = [0]

for _ in range(m):
    a, b = map(int, input().split())
    date.append(a)
    chapter.append(b)
    
dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if date[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-date[i]] + chapter[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])