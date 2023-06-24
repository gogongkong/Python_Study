'''
https://www.acmicpc.net/problem/16493
'''

'''
걸리는 일수 N, 챕터의 수 M 입력

챕터당 읽는데 걸리는수, 페이지수 입력

소요일수는 20보다 작음
페이지 수는 300보다 작음
'''

n, m = map(int, input().split())

date = [0]
chapter = [0]

for _ in range(m):
    a, b = map(int, input().split())
    date.append(a)
    chapter.append(b)

dp = [ [0] * (n+1) for _ in range(m+1) ]

for i in range(m+1):
    for j in range(n+1):
        if date[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - date[i]] + chapter[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])

