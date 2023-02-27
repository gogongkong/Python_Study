print("6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)")
a , b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d = 1
while d%a != 0 or d%b!= 0 or d%c != 0:
    d +=1

print(d)

print("6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)")
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d=[]

for i in range(24):
    d.append(0)
    # d[i] = 0

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end = ' ')

print("6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)")
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n-1 , -1, -1):
    print(a[i], end=' ')

print("6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)")
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

print(min(a))

print("6095[기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)")
d = []

for i in range(20): # 리스트 안에 리스트를 만들어 행렬 생성
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x,y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end = ' ')
    print()

print("6096[기초-리스트] 바둑알 십자 뒤집기(py)")

d = []
for i in range(20): # 바둑판 생성
    d.append([])
    for j in range(20):
        d[i].append(0)
    
for i in range(19): #돌깔기
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    for j in range(1,20):
        if d[j][y] == 0:
            d[j][y] = 1
        else: 
            d[j][y] = 0
        
        if d[x][j] == 0:
            d[x][j] = 1
        else: 
            d[x][j] = 0
    
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print()


print("2월4일 공부")

print("6095[기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)")
d = []
for i in range(20): # 바둑판 생성
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    d[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=' ')
    print()

print("6096[기초-리스트] 바둑알 십자 뒤집기(py)")
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])


n = int(input())
for i in range(n):
    x,y = input().split()
    x = int(x)
    y = int(y)
    for j in range(20):
        if d[j][y] == 0:
            d[j][y] = 1
        else:
            d[j][y] = 0
        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=' ')
    print()

print("6097[기초-리스트] 설탕과자 뽑기(py)")

h,w = map(int,input().split()) # 정수형 h, w 입력

d = [] # 공백의 리스트 생성

for i in range(h+1):# 입력받은 h,w로 공백의 행렬 생성
    d.append([])
    for j in range(w+1):
        d[i].append(0)

n = int(input()) # 막대를 몇개를 놓을지
for j in range(n):
    i, de, x, y = map(int,input().split()) # 막대 놓는 방식에 대한 입력
    for l in range(i):
        if de == 0: #가로
                d[x][y+l] = 1
        else: # 세로
                d[x+l][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(d[i][j],end=' ')
    print()


print("2월 5일")

#돌놓기
d = []
for i in range(20): # 19x19 바둑판 생성하기
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    d[x][y] = 1

for i in range(1,20): # 현재 바둑판 출력
    for j in range(1,20):
        print(d[i][j],end=' ')
    print()

#십자뒤집기
d = []
for i in range(20): # 바둑판 생성
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = list(map(int,input().split()))
    for j in range(19):
        d[i+1][j+1] = a[j]

n = int(input())
for i in range(n):
    x,y, = map(int, input().split())
    for j in range(20):
        if d[j][y] ==0:
            d[j][y] = 1
        else:
            d[j][y] = 0
        if d[x][j] == 0:
            d[x][j] =1
        else:
            d[x][j] =0

for i in range(1,20): # 바둑판 출력
    for j in range(1,20):
        print(d[i][j], end=' ')
    print()

코드업 6097번 설탕과자 뽑기
w, h = map(int, input().split())
de = []

# de=[[0]*(w) for i in range(h)]

for i in range(w+1):
    de.append([])
    for j in range(h+1):
        de[i].append(0)

n = int(input())
for j in range(n):
    i,d,x,y = map(int, input().split())
    for l in range(i):
        if d ==1:
            de[x+l][y] = 1
        else:
            de[x][y+l] = 1

for i in range(1,w+1):
    for j in range(1, h+1):
        print(de[i][j],end=' ')
    print()



d=[[0]*19 for i in range(19)]

w,h = map(int, input().split())
d=[[0]*(w+1) for i in range(h+1)]

for i in range(1,w+1):
    for j in range(1, h+1):
        print(d[i][j],end=' ')
    print()


print("6098 : [기초-리스트] 성실한 개미(py)")

w, h = list(map(int,input().split()))
d= []
for i in range(11):
    d.append([])
    for j in range(11):
        d[i].append(0)

for i in range(10):
    a = list(map(int, input().split()))
    for j in range(10):
        d[i+1][j+1] = a[j]

x = 2
y = 2

while True:
    if d[x][y] == 0:
        d[x][y] = 9
    elif d[x][y] == 2:
        d[x][y] = 9
        break
    
    if (d[x][y+1] == 1 and d[x+1][y] == 1) or (x==9 and y ==9) :
        break

    if d[x][y+1] != 1:
        y += 1
    elif d[x+1][y] !=1:
        x += 1

for i in range(1,11):
    for j in range(1,11):
        print(d[i][j],end=' ')
    print()


d = []
for i in range(11):
    d.append([])
    for j in range(11):
        d[i].append(0)

for i in range(10):
    a = list(map(int, input().split()))
    for j in range(10):
        d[i+1][j+1] = a[j]

x = 2
y = 2

while True:
    if d[x][y] ==0:
        d[x][y] =9
    elif d[x][y] ==2:
        d[x][y] =9
        break

    if (d[x][y+1] == 1 and d[x+1][y] == 1) or (x == 9 and y == 9):
        break

    if d[x][y+1] != 1:
        y += 1
    elif d[x+1][y] != 1:
        x += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end=' ')
    print()
