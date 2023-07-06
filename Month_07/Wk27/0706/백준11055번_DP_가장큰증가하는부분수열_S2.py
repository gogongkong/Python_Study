'''
https://www.acmicpc.net/problem/11055
'''

n = int(input())

data = list(map(int, input().split())) #[1, 100, 2, 50, 60, 3, 5, 6, 7, 8]

dp = [0] * (n)
dp[0] = data[0]

for i in range(1, n):
    for j in range(i+1):
        if data[i] > data[j]:
            dp[i] = max(dp[i], data[i] + dp[j])
        else:
            dp[i] = max(dp[i], data[i])
print(max(dp))