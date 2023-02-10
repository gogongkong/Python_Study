print("6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)")
h, b, c, s = map(int, input().split())
p = (h*b*c*s)/8/1024/1024
print(round(p,1),end = " MB")

print("6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)")
w,h,b= map(int, input().split())
p = (w*h*b)/8/1024/1024
print('%.2f'%p,end=' MB')

print("6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)")

n = int(input())
st = list(map(int, input().split()))

d=[]
for i in range(24):
    d.append(0)

for i in range(n):
    d[st[i]] += 1

for i in range(1,24):
    print(d[i], end=' ')

print("2월7일")

print("코드업 6098문제 복습")

d = []
for i in range(11): # 10x10 배열 생성
    d.append([])
    for j in range(11):
        d[i].append(0)

for i in range(10):
    x = list(map(int, input().split()))
    for j in range(10):
        d[i+1][j+1] = x[j]

x = 2
y = 2
while True:
    if d[x][y] == 2:
        d[x][y] =9
        break
    elif d[x][y] == 0:
        d[x][y] = 9
    
    if (x == 9 and y == 9) or (d[x][y+1] ==1 and d[x+1][y] == 1):
        break

    if d[x][y+1] !=1:
        y += 1
    elif d[x+1][y] != 1:
        x += 1

for i in range(1,11):
    for j in range(1,11):
        print(d[i][j], end = ' ')
    print()


print("코드업 6097번 복습")

grid = []
w,h = list(map(int, input().split()))
for i in range(w+1):
    grid.append([])
    for j in range(h+1):
        grid[i].append(0)

n = int(input())
for j in range(n):
    i, d, x, y = list(map(int, input().split()))
    for l in range(i):
        if d == 0:
            grid[x][y+l] = 1
        elif d ==1:
            grid[x+l][y] = 1


for i in range(w):
    for j in range(h):
        print(grid[i+1][j+1], end=' ')
    print()

print("이것이 코딩테스트다 with 파이썬")
#시간 복잡도
array = [3, 5, 1, 2, 4]    # 5개의 데이터
summary = 0             #합계를 저장할 변수

#모든 데이터를 하나씩 확인하여 합계를 계산
for x in array:
    summary += x

# 결과를 출력
print(summary) 
''' 5개의 데이터를 받아 차례로 5회 더해줌 연산횟수는 N에 비례 변수에 0을 대입하거나 출력하는것은
N의 커짐에 따라 작아지기에 무시할 수 있다'''

a= 5
b =7
print(a+b) # 시간 복잡도 1 O(1)


#아래 코드는 어떤 시간 복잡도를 가질지 생각해보자
array = [3, 5, 1, 2, 4] # 5개의 데이터 (N =5 )

for i in array:
    for j in array:
        temp = i*j
        print(temp)
#O(N^2)

import time
start_time = time.time()# 측정 시작

#프로그램 소스코드
end_time = time.time() #측정 종료
print("time:", end_time - start_time)#수행시간출력

# 선택정렬과 기본 정렬 라이브러리의 수행 시간 비교
from random import randint
import time

#배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1,100)) # 1부터 100사이의 랜덤한 정수

#선택 정렬 프로그램 성능 측저 
start_time = time.time()

#선택 정렬 프로그램 소스 코드
for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인데스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프

end_time = time.time() # 측정종료
print("선택 정렬 성능 측정: ", end_time - start_time) #수행 시간 출력

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1,100)) # 1부터 100까지의 랜덤한 정수

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time() # 측정 종료
print("기본 정렬 라이브러리 성능 측정: ", end_time - start_time) # 수행 시간 출력


print("예제3-1")
''' 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 짜리 동전이
무한히 존재한다고 가정 한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.'''

# 가장 큰 수 부터 거슬러 준다고 가정
n = int(input())
count = 0

coin = [500, 100, 50, 10]
for i in coin:
    count += n // i
    n %= i
print(count)


n = int(input())
count = 0
coin_type = [500, 100, 50, 10]
for coin in coin_type:
    count += n // coin
    n %= coin
print(count)

#큰수의 법칙(실전문제)
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[N-1]#첫번째로 큰수
second = data[N-2]#두번째로 큰수

result = 0
while True:
    for i in range(K):#가장 큰 수를 K번 더하기
        if M == 0:#M이 0이라면 반복문 탈출
            break
        result += first
        M -= 1#더할때 마다 1씩 빼기
    if M == 0:#M이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한번 더하기
    M -= 1 
print(result)

# 이해하고 다시 풀어보기
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result += second
    m-=1
print(result)

## 새로운 풀이
#n,m,k를 공백으로 구분하여 입력 받기
n,m,k = map(int, input().split())
#n개의 수를 공백을 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()#입력받은 수 정렬
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second #두번째로 큰 수 더하기

print(result)


print("6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)")
d= []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    # x, y = input().split()
    # x = int(x)
    # y = int(y)
    x, y = map(int, input().split())
    d[x][y] = 1


for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end= ' ')
    print()

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
sec = data[n-2]

count = int(m/(k+1))*k + m%(k+1)
#count += m%(k+1)

result = 0
result += (count)* first
result += (m-count)*sec

print(result)


print("큰수의 법칙 = gridy 복습")
# 방법1
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort()
first = data[n-1]
sec = data[n-2]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    
    if m == 0:
        break
    result += sec
    m-=1
print(result)


# 방법2
#int(m / (k+1)) *k + m % (k+1)
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort()
first = data[n-1]
sec = data[n-2]

count = int(m / (k+1)) *k + m % (k+1)
result += count*first
result += (m-count)*sec

print(result)


print("2월 9일 공부 시작")
#이코테 그리디 큰수의 법칙 실습 문제 복습

# while을 이용한 방법
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
sec = data[n-2]

index = 0

while True:
    for i in range(k):
        if m == 0:
            break
        index += first
        m -= 1
    
    if m == 0:
        break
    index += sec
    m -=1
print(index)

# 규칙을 알아내서 푸는 방법
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
sec = data[n-2]

index = 0

func = int(m/(k+1))*k + m%(k+1)
index += func*first
index += (m-func)*sec

print(index)

print("숫자 카드 게임")
#min과 max 함수 이용
n, m = list(map(int, input().split()))
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    minimum = min(data)
    result = max(result, minimum)

print(result)

#이중 for 이용 
n , m = list(map(int, input().split()))
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_data = 10001
    for j in data:
        min_data = min(min_data, j)
    # result = max(result, min_data)

print(min_data)

# 함수이용 다시 한번 풀어보기
n, m = map(int, input().split())
result = 0
for i in range(n): 
    data = list(map(int, input().split()))
    min_data = min(data)
    result = max(min_data, result)

print(result)

print("1이 될때 까지 p99")
# 내 풀이
n, k = map(int, input().split())
cnt = 0
while True:
    if n ==1:
        break
    elif n % k ==0:
        n = n/k
        cnt+=1
    elif n%k !=0:
        n -=1
        cnt+=1
print(cnt)

# 단순하게 푸는 방법
n, k = map(int, input().split())
result = 0

#n 이 k이상이라면 k로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n%k !=0:
        n-=1
        result += 1
    #k로 나누기
    n//=k
    result +=1

#마지막으로 남은 수에 대하여 1씩 빼기
while n>1:
    n -=1
    result += 1

print(result)

n, k = map(int, input().split())
result = 0

while True:
    #(n == k 로 나누어 떨어지는 수) 가 될때 까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target
    #n이 k보다 작을 때(더이상 나눌 수 없을때) 반복문 탈출
    if n < k:
        break
    #k로 나누기
    result +=1
    n//=k
#마지막으로 남은 수 에 대하여 1씩 빼기
result += (n-1)
print(result)



''' 실전문제 4 복습 '''
n, k = map(int, input().split()) # 2개 입력받음
count = 0 # 1 만들기 위한 횟수를 카운트할 변수
while True:
    if n ==1: # n이 1이면 반복문 탈출
        break
    elif n%k !=0: # n이 k로 나누어 떨어지지 않는지 확인 --> n%k가 0이 아니면 n에서 1을 뺀다
        n -=1
        count +=1
    elif n%k == 0: #n이 k로 나누어 떨어질때 n을 k로 나눔 --> n%k는 0
        n = n/k
        count +=1

print(count)

''' 개선점 = 29 5가 입력되면 1을 4번 빼야 하니 일일이 빼는 횟수를 줄여보기'''
n, k = map(int, input().split())
count = 0

while True:
    if n ==1: # n이 1이면 반복문 탈출
        break
    elif n%k != 0: #n이 k로 나누어 떨어지지 않을 때 나머지를 n에서 한번에 빼주고 나머지를 count에 더함
        i = n%k # n%k를 i라는 변수에 저장해서 진행하지 않고 n-=n&k 그리고 count += n%k를 하면 제대로 동작하지 않음
        n -= i
        count += i
    elif n%k ==0:
        n = n/k
        count +=1
print(count)

''' 예제 4-1 상하 좌우'''
# 내 풀이 == 완벽히 틀린느낌
N = int(input())
x =1
y =1
while True:
    loca = map(str, input().split())
    if loca == "\n":
        break
    elif loca == "R" and x !=5:
        x +=1
    elif loca == "R" and x ==5:
        x +=0
    elif loca == "L" and x !=1:
        x -=1
    elif loca =="L" and x ==1:
        x +=0
    elif loca =="U" and y !=1:
        y += 1
    elif loca =="U" and y==1:
        y +=0
    elif loca =="D" and y!=5:
        y-=1
    elif loca =="D" and y==5:
        y +=0

print(x, y)


'''풀이'''
# N입력받기
n = int(input())
x,y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

#이동 계획을 하나 씩 확인
for plan in plans:
    #이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if nx <1 or ny <1 or nx > n or ny >n :
        continue
    #이동 수행
    x,y = nx, ny
print(x, y)
        

''' 풀이 이해 후 풀어보기'''
n = int(input())
route = input().split()
x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_location = ['L', 'R', 'U', 'D']

for move in route:
    for i in range(len(move_location)):
        if move == move_location[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if nx <1 or ny <1 or nx > n or ny >n :
        continue
    
    x, y = nx, ny
print(x, y)


''' 예제 4-1 시각'''
#직접 풀어보기 - 3중 반복문으로 한개씩 세어보는 완전탐색으로 가자
n = int(input())
count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count +=1
print(count)


#풀이
n = int(input()) #시간 n입력
count = 0
for i in range(n+1):
    for j in range(60):
        for l in range(60):
            if '3' in str(i)+str(j)+str(l):
                count += 1

print(count)
