'''
https://www.acmicpc.net/problem/12852
'''

'''
1보다 크거나 같고 10^6보다 작거나 같은 자연수 N 입력

연산 횟수 최솟값 출력
N을 1로 만드는 방법에 포함되어 있는 수를 공백을 구분하여 순서대로 출력
순서대로 출력 == sort(reverse=true)
'''

n = int(input())

dp = [i for i in range(n+1)]
dp[1] = 0 # 1은 0가지임

result = [i for i in range(n+1)]
result[1] = 0

for i in range(2, n+1): # dp[1]은 이미 입력 되어서 2부터 시작
    dp[i] = dp[i-1] + 1
    result[i] = i-1
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
    print(result[now], end=' ')
    now = result[now]

