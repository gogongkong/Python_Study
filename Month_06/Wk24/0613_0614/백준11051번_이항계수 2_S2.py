'''
https://www.acmicpc.net/problem/11051
'''

import math

n, k = map(int, input().split())

result = (math.factorial(n) // (math.factorial(n-k) * math.factorial(k))) % 10007

print(result)