'''
https://www.acmicpc.net/problem/1699
'''

n = int(input())

dp = [i for i in range(n+1)]

for target in range(1,n+1):
    for prev in range(1,target):
        if prev * prev > target:
            break
        else:
            dp[target] = min(dp[target], dp[target - prev*prev] + 1)

print(dp[-1])