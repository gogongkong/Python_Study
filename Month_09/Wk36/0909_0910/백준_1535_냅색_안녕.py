'''
https://www.acmicpc.net/problem/1535
'''

n = int(input())

stamina = [0] + list(map(int, input().split()))
happy = [0] + list(map(int, input().split()))

dp = [ [0] * (101) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        # 현재 감당가능한 리스크가 취할 이득의 리스크보다 크다면 비교가능
        if stamina[i] <= j: 
            # 현재 가질 수 있는 이득을 포기 = dp[i-1][j]
            # 이득을 취하고 리스크도 가져가기 = dp[i-1][j-stamina[i]] + happy[i]
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-stamina[i]] + happy[i])
        # 현재 감당가능한 리스크의 총량이 곧 취할 이득의 리스크보다 작음 == 이득 포기
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])

