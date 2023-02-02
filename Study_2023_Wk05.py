# print("6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)")
# a , b, c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)

# d = 1
# while d%a != 0 or d%b!= 0 or d%c != 0:
#     d +=1

# print(d)

# print("6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)")
# n = int(input())
# a = input().split()

# for i in range(n):
#     a[i] = int(a[i])

# d=[]

# for i in range(24):
#     d.append(0)
#     # d[i] = 0

# for i in range(n):
#     d[a[i]] += 1

# for i in range(1, 24):
#     print(d[i], end = ' ')

# print("6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)")
# n = int(input())
# a = input().split()

# for i in range(n):
#     a[i] = int(a[i])

# for i in range(n-1 , -1, -1):
#     print(a[i], end=' ')

# print("6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)")
# n = int(input())
# a = input().split()

# for i in range(n):
#     a[i] = int(a[i])

# print(min(a))

# print("6095[기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)")
# d = []

# for i in range(20): # 리스트 안에 리스트를 만들어 행렬 생성
#     d.append([])
#     for j in range(20):
#         d[i].append(0)

# n = int(input())
# for i in range(n):
#     x,y = input().split()
#     d[int(x)][int(y)] = 1

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end = ' ')
#     print()

# print("6096[기초-리스트] 바둑알 십자 뒤집기(py)")

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
   
    

