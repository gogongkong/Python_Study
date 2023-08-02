'''
https://www.acmicpc.net/problem/2805
'''

# n 나무의 갯수
# m 원하는 길이
n, m = map(int, input().split())

datas = list(map(int, input().split()))

start, end = 0, max(datas)

while start <= end:
    result = 0
    mid = (start + end) // 2
    for data in datas:
        if data >= mid:
            result += data - mid
        
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(result)
print(end)
print(mid)