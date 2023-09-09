'''
https://www.acmicpc.net/problem/11052
'''

n = int(input())

data = [0] + list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], dp[i-j] + data[j])

print(dp[-1])