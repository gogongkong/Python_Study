'''
https://www.acmicpc.net/problem/11501
'''

tc = int(input())
result = []
for _ in range(tc):
    n = int(input())
    data = list(map(int, input().split()))
    answer = 0
    max_data = 0
    for i in range(n-1, -1, -1):
        if max_data < data[i]:
            max_data = data[i]
        else:
            answer += max_data - data[i]
    
    result.append(answer)

print(*result)