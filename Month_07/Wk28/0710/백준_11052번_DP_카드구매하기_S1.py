'''
https://www.acmicpc.net/problem/11052
'''

n = int(input())

p = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[-1])
print(dp)
'''
dp[1] 카드 1장살때
dp[1] = p1 + dp[0]

dp[2]
dp[0] + p2
dp[1] + p1

dp[3]
dp[0] + p3
dp[1] + p2
dp[2] + p1

dp[4]
dp[0] + p4
dp[1] + p3
dp[2] + p2
dp[3] + p1

'''