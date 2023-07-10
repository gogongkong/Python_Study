'''
https://www.acmicpc.net/problem/12852
'''

n = int(input())

dp = [i for i in range(n+1)]
dp[1] = 0

result = [i for i in range(n+1)]
result[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    result[i] = i - 1
    
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        result[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        result[i] = i//2
        
print(dp[n])
print(n,end=' ')

now = n

while result[now] != 0:
    print(result[now],end=' ')
    now = result[now]
