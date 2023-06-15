'''
https://www.acmicpc.net/problem/1912
'''

# 수열의 갯수 입력
# n = int(input())
# # 수열 입력
# data = list(map(int, input().split()))
# # dp 테이블 초기화
# dp = [0] * n
# dp[0] = data[0]

# for i in range(1,n):
#     if dp[i-1] + data[i] < dp[i-1]:
#         dp[i] = max(dp[i], dp[i-1] + data[i])
#     else:
#         dp[i] = dp[i-1] + data[i]

# print(dp)



# 수열의 갯수 입력
n = int(input())
# 수열 입력
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = data[0]
for i in range(1,n):
    dp[i] = max(data[i], dp[i-1] + data[i])

print(max(dp))