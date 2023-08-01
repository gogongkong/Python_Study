'''
https://www.acmicpc.net/problem/11057
'''
'''
n = 1 일 경우 하나당 하나씩이지만
2개인경우 0~9까지 모두 더한수 = 55
3개 부터 달라짐 2번째 수가 뭘 정하냐에 따라 그 뒤가 달라짐

    1   2    3    4
0   1   1    1    1
1   1   2    3    4
2   1   3    6    10
3   1   4    10   20
4   1   5    15   35
5   1   6    21
6   1   7    28
7   1   8    36
8   1   9    45
9   1   10   55

점화식 도출
3자리수라고 가정
dp[i][j] = dp[i][j-1] + dp[i-1][j]
dp[i][0] = 1
'''

NUM = 10007 
n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2,n+1):
    dp[i][0] = 1
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

result = 0
for i in range(10):
    result += dp[n][i]
print(result%NUM)