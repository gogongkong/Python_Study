'''
https://www.acmicpc.net/problem/19637
'''  
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [input().split() for _ in range(n)]

def check(data, answer):
    start, end = 0, len(data) - 1
    result = 0
    
    while start<= end:
        mid = (start + end) // 2
        if int(data[mid][1]) >= answer:
            end = mid -1
            result = mid
        else:
            start = mid + 1
    
    return result

result = []
for i in range(m):
    answer = int(input())
    result.append(data[check(data, answer)][0])

for i in result:
    print(i)