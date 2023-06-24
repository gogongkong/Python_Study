'''
https://www.acmicpc.net/problem/12852
'''

'''
1보다 크거나 같고 10^6보다 작거나 같은 자연수 N 입력

연산 횟수 최솟값 출력
N을 1로 만드는 방법에 포함되어 있는 수를 공백을 구분하여 순서대로 출력
순서대로 출력 == sort(reverse=true)
'''

x = int(input())

dp = [i for i in range(x+1)]
dp[1] = 0
result = [i for i in range(x+1)]
result[1] = 0

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    result[i] = i-1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        result[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        result[i] = i//2

# result = [0, 1, 1, 1, 3, 4, 2, 6, 4, 3, 9]

print(dp[x])
print(x,end=' ')

now = x
while result[now] != 0:
    print(result[now], end=' ')
    now = result[now]

