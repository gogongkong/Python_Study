'''
https://www.acmicpc.net/problem/15989
'''

T = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

result = []
for _ in range(T):
    result.append(dp[int(input())])

print(result)