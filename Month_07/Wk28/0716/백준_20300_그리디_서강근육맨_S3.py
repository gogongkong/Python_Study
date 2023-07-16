'''
https://www.acmicpc.net/problem/20300
'''

n = int(input())

data = list(map(int, input().split()))
data.sort()
result = []

if n % 2 == 1:
    result.append(max(data))
    data.remove(max(data))

for i in range((n//2+1)):
    result.append(data[i] + data[len(data) -i-1])
print(max(result))
