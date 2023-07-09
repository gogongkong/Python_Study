'''
https://www.acmicpc.net/problem/1535
'''

n = int(input()) #사람의 수

stemina = [0] + list(map(int, input().split())) # 소모되는 체력
happy = [0] + list(map(int, input().split())) # 얻는 행복

dp = [[0] * 101 for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, 101):
        if stemina[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - stemina[i]] + happy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])