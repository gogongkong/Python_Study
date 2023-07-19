'''
https://www.acmicpc.net/problem/11501
'''

tc = int(input())
answer = []
for _ in range(tc):
    # 기간 
    date = int(input())
    # 날짜별 주가
    data = list(map(int, input().split()))
    result = 0
    max_value = 0
    for i in range(date-1, -1, -1):
        if  data[i] > max_value:
            max_value = data[i]
        else:
            result += max_value - data[i]
    answer.append(result)

for i in answer:
    print(i)