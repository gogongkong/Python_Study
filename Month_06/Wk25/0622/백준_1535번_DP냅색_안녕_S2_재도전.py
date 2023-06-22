'''
https://www.acmicpc.net/problem/1535
'''

n = int(input())

stamina = [0] + list(map(int, input().split())) # 체력
happy = [0] + list(map(int, input().split())) # 행복

dp = [[0] * 101 for _ in range(n+1)] # DP 테이블 초기화

for i in range(1, n+1): # 사람의 수 만큼 반복
    for j in range(1, 101): # 체력만큼 반복
        if stamina[i] <= j: # 현재 체력이 소모될 체력보다 작다면
            # 이전의 값에서 제한사항을 제외한 값과 이전의값에서 제한사항을 뺀것에 이득을 더한것을 비교하여 더 큰쪽을 선택한다.
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - stamina[i]] + happy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])

