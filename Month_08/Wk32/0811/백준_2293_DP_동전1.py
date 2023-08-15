'''
https://www.acmicpc.net/problem/2293
'''

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])