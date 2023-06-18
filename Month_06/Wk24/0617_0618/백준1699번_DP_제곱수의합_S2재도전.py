'''
https://www.acmicpc.net/problem/1699
'''

n = int(input()) # 자연수 N 입력

dp = [i for i in range(n+1)]

for current in range(1, n+1):
    for prev in range(1,current):
        if prev * prev > current:
            break
        else:
            dp[current] = min(dp[current], dp[current - prev*prev] + 1)

print(dp[n])