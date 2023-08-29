'''
https://www.acmicpc.net/problem/4811
'''

dp = [[0] * 31 for _ in range(31)]
for i in range(1,31):
    dp[0][i] = 1
for i in range(1,31):
    for j in range(i, 31):
        dp[i][j] += dp[i][j-1] + dp[i-1][j]

while True:
    med = int(input())
    if med == 0:
        break
    print(dp[med][med])