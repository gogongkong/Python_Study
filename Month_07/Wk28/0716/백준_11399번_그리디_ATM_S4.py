'''
https://www.acmicpc.net/problem/11399
'''

n = int(input())

p = list(map(int, input().split()))

p.sort()
result = [p[0]]

for i in range(1,n):
    result.append(result[i-1] + p[i])

print(sum(result))