'''
https://www.acmicpc.net/problem/1697
'''

'''
수빈이의 위치 N, 동생의 위치 K 입력

걷기 = N+1 혹은 N-1, 순간이동 = 2 * N

동생을 찾는 가장 빠른 시간을 출력
'''

'''
실패

1. BFS로 푸는 방법을 알지 못하였음
2. DP로 풀 수 있을것이라 생각하였지만 N-1에 대한 가정을 하지 않았음
3. DP로 풀 수 있다면 DP로 분류되었을것 하지만 그렇지 않았음
'''


n, k = map(int, input().split())

dp = [ i for i in range(k+1) ]

for i in range(1, k+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1

print(dp[n])
