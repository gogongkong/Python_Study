h, m, s = input().split(':')
print(m)

w1, w2 = input().split()
s = w1 + w2
print(s)

print("정수 2개를 입력받아\
합을 출력하는 프로그램을 작성해보자.")

n1, n2 = input().split()
s = int(n1)+int(n2)
print(s)

print("실수 2개를 입력받아\
합을 출력하는 프로그램을 작성해보자.")

n1 = input()
n2 = input()
s = float(n1) + float(n2)
print(s)

print("10진수를 입력받아 16진수(hexadecimal)로 출력해보자.")

a = input()
n = int(a)

print('%x'%n)

n = 10
a =10
print("%x"%n)
print("{0}, 16진수 , {1}, 10진수".format('%x'%n, a))

a = input()
n = int(a)
print("%X"%n)

print("[기초-값변환] 16진 정수 입력받아 8진수로 출력하기(설명)(py)")
a = input()
n = int(a, 16)
print("%o"%n)

print("[기초-값변환] 영문자 1개 입력받아 10진수로 변환하기(설명)(py)")
n = ord(input())
print(n)
	
print("[기초-값변환] 정수 입력받아 유니코드 문자로 변환하기(설명)(py)")
n = int(input())
print(chr(n))

print("[기초-산술연산] 정수 1개 입력받아 부호 바꾸기(설명)(py)")
n = int(input())
print(-n)

print("[기초-산술연산] 문자 1개 입력받아 다음 문자 출력하기(설명)(py)")
a = input()
a = ord(a)
print(chr(a+1))

print("[기초-산술연산] 정수 2개 입력받아 차 계산하기(설명)(py)")
a, b = input().split()
n = int(a)-int(b)
print(n)

print("[기초-산술연산] 실수 2개 입력받아 곱 계산하기(설명)(py)")
a, b = input().split()
n = float(a)*float(b)
print(n)

print("[기초-산술연산] 단어 여러 번 출력하기(설명)(py)")
w, b = input().split()
print(w*int(b))

print("[기초-산술연산] 문장 여러 번 출력하기(설명)(py)")
num = input()
chr = input()

print(int(num) * chr)

print("[기초-산술연산] 정수 2개 입력받아 거듭제곱 계산하기(설명)(py)")
a, b =input().split()
n = int(a)**int(b)
print(n)

print("[기초-산술연산] 실수 2개 입력받아 거듭제곱 계산하기(py)")
a, b =input().split()
n = float(a)**float(b)
print(n)

print("[기초-산술연산] 정수 2개 입력받아 나눈 몫 계산하기(설명)(py)")
a, b =input().split()
n = int(a)//int(b)
print(n)
a, b =input().split()
n = int(a)%int(b)
print(n)

print("[기초-값변환] 실수 1개 입력받아 소숫점이하 자리 변환하기(설명)(py)")
a = float(input())
a = round(a, 2)
print(a)

print("[기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)")
a, b = input().split()
c = float(a)/float(b)
print(format(c,".3f"))

print("[기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)")
a, b = input().split()
a= int(a)
b= int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(a/b, 2))

print("데스크톱 앱 커밋 테스트")
print("데스크톱 앱 레파지토리 이름변경 테스트")

print("[기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)")

a, b, c = input().split()
a=int(a)
b=int(b)
c=int(c)
print(a+b+c, format((a+b+c)/3,".2f"))

print("[기초-비트시프트연산] 정수 1개 입력받아 2배 곱해 출력하기(설명)(py)")
a = input()
a = int(a)
print(a*2)
print(a<<1)

print("[기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기(설명)(py)")
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)

print("[기초-비교연산] 정수 2개 입력받아 비교하기1(설명)(py)")
a, b =input().split()
a = int(a)
b = int(b)
print(a<b)

print("[기초-비교연산] 정수 2개 입력받아 비교하기2(설명)(py)")
a, b =input().split()
a = int(a)
b = int(b)
print(a==b)
    
print("[기초-비교연산] 정수 2개 입력받아 비교하기3(설명)(py)")
a, b =input().split()
a = int(a)
b = int(b)
print(b>=a)

print("[기초-비교연산] 정수 2개 입력받아 비교하기4(설명)(py)")
a, b =input().split()
a = int(a)
b = int(b)
print(a!=b)

print("[기초-논리연산] 정수 입력받아 참 거짓 평가하기(설명)(py)")
a = int(input())
print(bool(a))

print("[기초-논리연산] 참 거짓 바꾸기(설명)(py)")
a = bool(int(input()))
print(not a)

print("[기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)")
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

print("[기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)")
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

print("[기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)")
print("2개의 정수값이 입력될 때,\
      그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.")
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a^b)
print((a and (not b)) or ((not a) and b))
print(bool(int(a)) != bool(int(b)))

print("[기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)")
print("2개의 정수값이 입력될 때,\
그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.")

a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(a == b)

print("[기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)")
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print(not a and not b)

print("[기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)(py)")
a = input()
a = int(a)
print(~a)

print("[기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)(py)")
a, b = input().split()
a = int(a)
b = int(b)
print(a & b)

print("6061[기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)(py)")
a, b = input().split()
a = int(a)
b = int(b)
print(a | b)

print("6062[기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)(py)")
a, b = input().split()
a = int(a)
b = int(b)
print(a ^ b)

print("6063[기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)")
a, b = input().split()
a = int(a)
b = int(b)
if a > b:
    print(a)
else:
    print(b)
c = (a if (a>=b) else b)
print(c)

print("6064[기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)")
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = a if (a<b) else b
e = d if (d<c) else c
print(e)

print("6065[기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)(py)")
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0:
    print(a)
if b%2 ==0:
    print(b)
if c%2 ==0:
    print(c)

print("6066[기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)")
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0:
    print("even")
else:
    print("odd")
if b%2 ==0:
    print("even")
else:
    print("odd")
if c%2 ==0:
    print("even")
else:
    print("odd")

print("6067[기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)")
a = int(input())
if a%2 ==0 and a<0:
    print("A")
elif a%2 !=0 and a<0:
    print("B")
elif a%2 ==0 and a>0:
    print("C")
elif a%2 !=0 and a>0:
    print("D")

print("6068[기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)")
a = int(input())
if 90 <= a <= 100:
    print("A")
elif 70<= a <= 89:
    print("B")
elif 40 <= a <= 69:
    print("C")
else:
    print("D")

print("6069[기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)")
a = input()
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

print("6070[기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)")
a = int(input())
if a == 12 or a == 1 or a == 2:
    print("winter")
elif a ==3 or a == 4 or a == 5:
    print("spring")
elif a == 6 or a == 7 or a ==8:
    print("summer")
elif a ==9 or a == 10 or a == 11:
    print("fall")

print("6071[기초-반복실행구조] 0 입력될 때까지 무한 출력하기(설명)(py)")
n=1
while n != 0:
    n = int(input())
    if n != 0:
        print(n)

print("6072[기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)")

n = int(input())
while n != 0:
    if n != 0:
        print(n)
        n = n-1
    # elif n ==0:
    #     print(n)
    #     break

print("6073[기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)")

n = int(input())
while n != 0:
    n = n-1
    print(n)

print("6074[기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)")

a = ord(input()) # a = 97
t = ord('a')
while t <=a:
    print(chr(t),end=' ')
    t+=1

print("6075[기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)")
n = int(input())
c = 0
while c !=n+1:
    print(c)
    c +=1

n = int(input())
c = 0
while c <=n:
    print(c)
    c +=1

print("6076[기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)")
n = int(input())
for i in range(n+1):
    print(i)

print("6077[기초-종합] 짝수 합 구하기(설명)(py)")
n = int(input())
c =0
for i in range(n+1):
    if i%2 == 0:
        c = i+c
print(c)

print("6078[기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)")
n = 'a'
while n != 'q':
    n = input()
    if n != 'q':
     print(n)
print('q')

while True:
   n = input()
   print(n)
   if n == 'q':
    break

print("6079[기초-종합] 언제까지 더해야 할까?(py)")
n = int(input())
a = 1
sum = 0
while sum < n:
    sum += a
    a += 1
print(a-1)