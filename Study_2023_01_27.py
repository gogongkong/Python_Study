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
