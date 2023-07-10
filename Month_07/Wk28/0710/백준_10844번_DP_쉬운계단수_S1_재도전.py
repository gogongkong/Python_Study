'''
https://www.acmicpc.net/problem/10844
'''

RES = 1000000000

n = int(input())

dp = [[0] * (10) for _ in range(n+1)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

result = 0
for i in range(10):
    result += dp[n-1][i]

print(result % RES)



