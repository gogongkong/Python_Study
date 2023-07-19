'''
https://www.acmicpc.net/problem/21314
'''

# 풀이 접근
# 최솟값 : M과 K를 최대한 분리
# 최댓값 : M과 K를 합칠 수 있는 만큼 합치기
# 숫자 변환
# EX1 : MM = 10^i (i = len(MM))
# EX2 : MMK = 5* 10^i

data = list(input())

##### 최소값 #####
answer = []
m1 = -1
if data[0] == 'K':
    answer.append(5)
elif data[0] =='M':
    m1 += 1
    
for i in range(1, len(data)):
    if data[i] == 'K':
        if m1 >= 0:
            answer.append(10**m1)
        answer.append(5)
        m1 = -1
    elif data[i] == 'M':
        m1 += 1
        
if m1 != -1:
    answer.append(10**m1)
for i in range(len(answer)):
    if i == len(answer)-1:
        print(answer[i])
    else:
        print(answer[i],end='')


##### 최대값 #####
answer = []
m2 = -1

if data[0] == 'K':
    answer.append(5)
elif data[0] =='M':
    m2 += 1

for i in range(1, len(data)):
    if data[i] == 'K' and m2 >= 0:
        answer.append(5 * 10 **(m2+1))
        m2 = -1
    elif data[i] =='K' and m2 == -1:
        answer.append(5)
    elif data[i] == 'M':
        m2 += 1
if m2 != -1:
    answer.append(10**m2)

for i in answer:
    print(i,end='')