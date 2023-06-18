'''
https://www.acmicpc.net/problem/11055
'''
# 수열의 크기 입력
n = int(input())
# 수열 입력
data = list(map(int, input().split()))

dp = [0] * n
dp[0] = data[0]

for target in range(1,n):
    for comp in range(target):
        if data[target] > data[comp]:
            dp[target] = max(dp[target], dp[comp] + data[target])
        else:
            dp[target] = max(dp[target], data[target])

print(max(dp))

