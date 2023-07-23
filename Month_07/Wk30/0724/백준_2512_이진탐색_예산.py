'''
https://www.acmicpc.net/problem/2512
'''

n = int(input())
data = list(map(int, input().split()))
m = int(input())
start, end = 0, max(data)


if sum(data) <= m:
    print(max(data))

else:
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in data:
            total += min(i, mid)
        
        if total > m:
            end = mid -1
        else:
            start = mid +1
    print(end)