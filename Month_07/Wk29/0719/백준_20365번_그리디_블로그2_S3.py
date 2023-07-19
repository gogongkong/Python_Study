'''
https://www.acmicpc.net/problem/20365
'''

# 풀이 접근
# dictionary 형태로 'B', 'R' 두가지 인자를 두고
# B -> R 혹은 R -> B로 변할때 하나씩 count
# 반복이 끝나고 가장 작은 값을 출력

# 문제의 수 N 입력
n = int(input())

dict = { 'B' : 1, 'R' : 1 }

data = list(input())
for i in range(n):
    if i == 0:
        dict[data[i]] += 1
    else:
        if data[i] != data[i-1]:
            dict[data[i]] +=1
            
print(min(dict['B'], dict['R']))
