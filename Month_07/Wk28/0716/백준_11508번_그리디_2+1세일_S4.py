'''
https://www.acmicpc.net/problem/11508
'''

n = int(input())

milks = []
for _ in range(n):
    milks.append(int(input()))

milks.sort(reverse=True)
result = 0
for i in range(len(milks)):
    if i % 3 != 2:
        result += milks[i]

print(result)
