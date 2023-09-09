'''
https://www.acmicpc.net/submit/16493/63384023
'''
n, m = map(int, input().split())

date = [0]
chapter = [0]

for _ in range(m):
    a, b = map(int, input().split()) # a 챕터당 소요일 수(소모값), b 페이지 수(이득)
    date.append(a)
    chapter.append(b)

result = [[0] * (n+1) for _ in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if date[i] <= j:
            result[i][j] = max(result[i-1][j], result[i-1][j - date[i]] + chapter[i])
        else:
            result[i][j] = result[i-1][j]

print(result[-1][-1])


n,m = map(int, input().split())
chapter = [0]
date = [0]

for _ in range(m):
    a, b = map(int, input().split())
    date.append(a)
    chapter.append(b)

dp = [[0] * (n+1) for _ in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if date[i] <= i:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-date[i]] + chapter[i])
        else:
            dp[i][j] = dp[i-1][j]