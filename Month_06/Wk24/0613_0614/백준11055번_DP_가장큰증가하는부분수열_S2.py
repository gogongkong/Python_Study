'''
https://www.acmicpc.net/problem/11055
'''

n = int(input())

data = list(map(int, input().split()))

d = [0] * n
d[0] = data[0]

for i in range(1,n):
    for j in range(i):
        if data[i] > data[j]:
            d[i] = max(d[i], d[j] + data[i])
        else:
            d[i] = max(d[i], data[i])

print(max(d))