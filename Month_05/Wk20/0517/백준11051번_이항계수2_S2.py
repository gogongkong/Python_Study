'''
https://www.acmicpc.net/problem/11051

예제 입력 1 
5 2
예제 출력 1 
10

'''

'''
이항계수 공식
상단 n 하단 r일때 = n! // r!(n-r)!
'''

import math

n, k = map(int, input().split())

result = (math.factorial(n) // (math.factorial(k) * math.factorial(n-k))) % 10007

print(result)