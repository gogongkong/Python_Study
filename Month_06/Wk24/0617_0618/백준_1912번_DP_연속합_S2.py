'''
https://www.acmicpc.net/problem/1912
'''
# 수열의 갯수 입력
n = int(input())
# 수열 입력
data = list(map(int, input().split()))

dp = [0] * n # dp 테이블 초기화
dp[0] = data[0] # 첫번째 인덱스는 수열의 첫번째 수

for i in range(1,n):
    if data[i] < dp[i-1] + data[i]:
        dp[i] = dp[i-1] + data[i]
    else:
        dp[i] = data[i]

print(max(dp))
