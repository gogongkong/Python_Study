print("6080[기초-종합] 주사위 2개 던지기(설명)(py)")

n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
for i in range(1, n1+1):
    for l in range(1, n2+1):
        print(i, l)

print("6081[기초-종합] 16진수 구구단 출력하기(py)")
n = int(input(), 16)
for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

for i in range(1,16):
    print("%X*%X=%X"%(n,i,n*i))

print("6082[기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)")
n = int(input())
for i in range(1,n+1):
    if i%10 == 3 or i%10 == 6 or i%10 ==9:
        print("X",end=' ')
    else:
        print(i,end=' ')

print("6083[기초-종합] 빛 섞어 색 만들기(설명)(py)")
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
cnt = 0
for i in range(0,r):
    for j in range(0, g):
        for l in range(0, b):
            print(i,j,l)
            cnt +=1
print(cnt)

print("6084[기초-종합] 소리 파일 저장용량 계산하기(py)")
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
print(round(h*b*c*s/8/1024/1024,1),"MB")

print("6085[기초-종합] 그림 파일 저장용량 계산하기(py)")
w,h,b = input().split()
w = int(w)
h = int(h)
b = int(b)
Q = round(w*h*b/8/1024/1024,2)
print('%.2f'%Q,"MB")

print("6086[기초-종합] 거기까지! 이제 그만~(설명)(py)")
n = int(input())
cnt = 0
for i in range(1,n+1):
    if cnt >= n:
        break
    else:
        cnt+=i
print(cnt)