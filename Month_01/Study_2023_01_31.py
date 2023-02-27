print("6087[기초-종합] 3의 배수는 통과(설명)(py)")

n = int(input())

for i in range(1,n+1):
    if i%3 ==0:
        continue
    else:
        print(i, end=' ')

print("6088[기초-종합] 수 나열하기1(py)")
a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)
for i in range(1,n):
    a=a+d
print(a)

print("6089[기초-종합] 수 나열하기2(py)")
a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

for i in range(1, n):
    a *= r
print(a)

print("6090[기초-종합] 수 나열하기3(py)")
a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1,n):
    a = a*m+d
print(a)

print("6091[기초-종합] 함께 문제 푸는 날(설명)(py)")
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

d=1
while d%a != 0 or d%b != 0 or d%c != 0:
    d+=1
print(d)

print("6092[기초-리스트] 이상한 출석 번호 부르기1(설명)(py)")
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1
for i in range(1,24):
    print(d[i], end = ' ')

print("6093[기초-리스트] 이상한 출석 번호 부르기2(py)")
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

for i in range(n-1, -1, -1) :
  print(a[i], end=' ')

print("6094[기초-리스트] 이상한 출석 번호 부르기3(py)") 
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

print(min(a))
