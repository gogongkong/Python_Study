'''
https://www.acmicpc.net/problem/10844
'''
'''
0   1   2   3

0   1   2   3
1   2   3   6
2   2   4   7
3   2   4   8
4   2   4   8
5   2   4   8
6   2   4   8
7   2   4   8
8   2   3   6
9   1   2   3

if j = 1 ~ 8
[i][j] += [i-1][j-1] + [i-1][j+1]

elif j = 0
[i][j] += [i-1][j+1]

elif j = 9
[i][j] += [i-1][j-1]
'''

DIV = 1000000000

# 자릿수 입력
n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
# 첫번째 dp 테이블( 한자릿수 ) 초기화
for i in range(1,10):
    dp[0][i] = 1

for i in range(1,n):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

result = 0

for i in range(10):
    result += dp[n-1][i]

print(result % DIV)



