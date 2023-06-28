'''
https://www.acmicpc.net/problem/20300
'''

n = int(input())

data = list(map(int, input().split()))
data.sort()

result = []

if n % 2 == 1:
    result.append(data[-1])
    data.remove(data[-1])

for i in range(n//2):
    result.append(data[i] + data[-i-1])

print(max(result))