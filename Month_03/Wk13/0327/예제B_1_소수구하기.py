'''
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오

[입력 조건]
    - 첫째 줄에 자연수 M과 N이 빈칼을 사이에 두고 주어진다.
        (1 <= M <= N <= 1,000,000)
    - 단. M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
[출력 조건]
    - 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

[입력 예시]
3 16

[출력 예시]
3
5
7
11
13
'''

import math

m,n = map(int, input().split())

arr = [True for i in range(100001)] # 처음엔 모든 수가 소수(true)인 것으로 초기화(0과 1은 제외)
arr[1] = 0

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n))+1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1


for i in range(m, n+1):
    if arr[i]:
        print(i)