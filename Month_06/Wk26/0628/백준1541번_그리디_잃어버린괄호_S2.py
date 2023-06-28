'''
https://www.acmicpc.net/problem/1541
'''

data = input().split('-') # '-'를 기준으로 분리
result = 0 # 결과를 담을 변수

for i in data[0].split('+'):
    result += int(i)

for i in data[1:]:
    for j in i.split('+'):
        result -= int(j)
print(result)