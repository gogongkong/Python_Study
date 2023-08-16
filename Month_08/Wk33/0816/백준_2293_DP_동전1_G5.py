'''
https://www.acmicpc.net/problem/2293
'''

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

'''
    0   1   2   3   4   5   6   7   8   9   10
1   1   1   1   1   1   1   1   1   1   1   1
2   1   1   2   2   3   3   4   4   5   5   6
5   1   1   2   2   2   4   5   6   7   8   10
'''
dp = [0] * (k+1)
dp[0] = 1
for i in coins:
    for j in range(i,k+1):
        dp[j] = dp[j] + dp[j-i]

print(dp[k])