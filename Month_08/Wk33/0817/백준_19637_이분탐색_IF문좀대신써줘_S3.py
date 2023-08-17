'''
https://www.acmicpc.net/problem/19637
'''

n, m = map(int, input().split())
status = [input().split() for _ in range(n)]
datas = [int(input()) for _ in range(m)]

# status[1]을 가지고 이분탐색을 진행

result = []
for data in datas:
    answer = 0
    start, end = 0, len(status) - 1

    while start <= end:
        mid = (start + end) // 2
        if data <= int(status[mid][1]):
            end = mid -1
            answer = end
        else:
            start = mid + 1
    
    result.append(answer)

for i in result:
    print(status[i+1][0])