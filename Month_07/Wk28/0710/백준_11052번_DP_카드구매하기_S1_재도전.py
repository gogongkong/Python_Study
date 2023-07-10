'''
https://www.acmicpc.net/problem/11052
'''

'''
dp[1] = max(dp[0] + p1)
dp[2] = max(dp[0] + p2, dp[1] + p1)
dp[3] = max(dp[0] + p3, dp[1] + p2, dp[2] + p1)
dp[4] = max(dp[0] + p4, dp[1] + p3, dp[2] + p2, dp[3] + p1)
'''

n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], p[j] + dp[i-j])
        
print(dp)