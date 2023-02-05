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
