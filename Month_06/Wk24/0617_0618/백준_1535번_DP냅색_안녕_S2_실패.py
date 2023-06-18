'''
https://www.acmicpc.net/problem/1535
'''
import copy
n = int(input()) # 사람의 수 입력

data = []
data.append(list(map(int, input().split()))) # data[0][] = 체력
data.append(list(map(int, input().split()))) # data[1][] = 기쁨

# dp 테이블 초기화
# dp 테이블 초기화
# dp[0][] = 체력 / dp[1][] = 기쁨
dp = [[0] * n for _ in range(2)] 
dp = copy.deepcopy(data)


for i in range(1,n):
    if data[0][i] + dp[0][i-1] < 100:
        dp[1][i] = max(data[1][i], dp[1][i-1] + data[1][i])
        dp[0][i] = dp[0][i-1] + data[0][i]
    elif data[0][i] >= 100 or dp[0][i-1] + data[0][i] >= 100:
        dp[1][i] = data[1][i]

if len(data[0]) == 1 and data[0][0] >= 100:
    print(0)
else:
    print(max(dp[1]))

'''
오답이 나온 예제입력
8
100 26 13 17 24 33 100 99
34 56 21 1 24 34 100 99
정답 출력 = 135
내 출력 = 102
'''
