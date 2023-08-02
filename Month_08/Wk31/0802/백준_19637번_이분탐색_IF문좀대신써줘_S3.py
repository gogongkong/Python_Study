'''
https://www.acmicpc.net/problem/19637
'''  
n, m = map(int, input().split())
status = [list(input().split()) for _ in range(n)]

start, end = 0, len(status) -1
result = []

def check(data, status):
    start, end = 0, len(status) -1
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        if data <= int(status[mid][1]):
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer

for i in range(m):
    data = int(input())
    result.append(status[check(data,status)][0])
print(result)