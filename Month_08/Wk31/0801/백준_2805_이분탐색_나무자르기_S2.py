'''
https://www.acmicpc.net/problem/2805
'''

n, m = map(int, input().split())

data = list(map(int, input().split()))

start, end = 0, max(data)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in data:
        if i >= mid:
            result += i - mid
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)