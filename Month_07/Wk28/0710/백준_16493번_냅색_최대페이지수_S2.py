'''
https://www.acmicpc.net/problem/16493
'''


# 남은 기간 N, 챕터의 수 M
n, m = map(int, input().split())

date = [0]
chapter = [0]

# 챕터의 수 만큼 입력
for _ in range(m):
    a, b = map(int, input().split())
    date.append(a)
    chapter.append(b)

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
    for j in range(1, n+1):
        if date[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - date[i]] + chapter[i])

        else:
            dp[i][j] = dp[i-1][j]


print(dp[-1][-1])