'''
https://www.acmicpc.net/problem/11055
'''

n = int(input()) # 수열의 크기 입력

data = list(map(int, input().split())) # 수열 입력

dp = [0] * n
dp[0] = data[0] # dp테이블 초기화

for current in range(1,n):
    for prev in range(current):
        if data[current] > data[prev]:
            dp[current] = max(dp[current], dp[prev] + data[current])
        else:
            dp[current] = max(dp[current], data[current])

print(max(dp))