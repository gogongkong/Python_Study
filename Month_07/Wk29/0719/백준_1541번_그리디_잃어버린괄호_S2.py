'''
https://www.acmicpc.net/problem/1541
'''

# 풀이 접근
# '-'를 기준으로 입력을 나눠 받는다(split('-'))
# '-'앞의 수는 모두 더하고, '-'뒤의 수를 따로 모두 더해 앞에수에서 빼준다

# 데이터 입력
data = input().split('-')
# 정답을 입력받을 변수 result
result = 0

for i in data[0].split('+'):
    result += int(i)
for j in range(1,len(data)):
    for k in data[j].split('+'):
        result -= int(k)

print(result)
    
    
    

