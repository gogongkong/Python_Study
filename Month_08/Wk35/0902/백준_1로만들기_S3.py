'''
https://www.acmicpc.net/problem/1463
'''

# 3으로 나누어 떨어지면 3으로 나눔
# 2로 나누어 떨어지면 2로 나눔
# 다 안되면 1을 뺌

n = int(input())
dp = [0] * (n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])