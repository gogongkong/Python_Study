'''
https://www.acmicpc.net/problem/2217
'''


# 모든 로프를 사용해야 할 필요가 없다.
n = int(input())

ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort()

result = []
for rope in ropes:
    result.append(rope * n)
    n -=1

print(max(result))
