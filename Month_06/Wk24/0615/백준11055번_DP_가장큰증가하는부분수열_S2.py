'''
https://www.acmicpc.net/problem/11055
'''

# 풀이 방식
# 수열의 첫째항부터 확인하고
# 해당 항까지의 가장 큰 증가하는 부분수열 합을 dp테이블에 저장
# 항을 증가하며 dp 테이블 갱신

n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
dp[0] = data[0]

for target in range(1,n):
    for comp in range(target):
        # 현재 항이 비교 항보다 큰 경우 (== 증가하는 부분 수열인 경우)
        if data[target] > data[comp]:
            dp[target] = max(dp[target], dp[comp] + data[target])
        else:
            dp[target] = max(dp[target], data[target])

print(max(dp))
