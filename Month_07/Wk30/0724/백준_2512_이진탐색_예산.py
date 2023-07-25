'''
https://www.acmicpc.net/problem/2512
'''

n = int(input())
data = list(map(int, input().split()))
m = int(input())

result = 0
start, end = 0, max(data)

if sum(data) <= m:
    print(max(data))

else:
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for i in data:
            result += min(i, mid)
        
        if result > m:
            end = mid -1
        else:
            start = mid + 1
    
    print(end)