'''
https://www.acmicpc.net/problem/11501
'''

tc = int(input())
result = []
for _ in range(tc):
    n = int(input())

    data = list(map(int, input().split()))

    max_data = 0
    answer = 0
    for i in range(n-1, -1, -1):
        if data[i] > max_data:
            max_data = data[i]
        else:
            answer += max_data - data[i]
    
    result.append(answer)

print(result)