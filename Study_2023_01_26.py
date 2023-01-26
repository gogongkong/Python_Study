print("Hello")


# 이번에는 공백( )을 포함한 문장을 출력한다.
# 다음 문장을 출력해보자.

# Hello World
# (대소문자에 주의한다.)

print("Hello World")

# 이번에는 줄을 바꿔 출력하는 출력문을 연습해보자.
# 다음과 같이 줄을 바꿔 출력해야 한다.

# Hello
# World
# (두 줄에 걸쳐 줄을 바꿔 출력)

print("Hello")
print("World")

print("'Hello'")

print('"Hello World"')

print("\"!@#$%^&*()'")

print('print("Hello\\nWorld")')



c = input()
print(c)


print("변수에 정수값을 저장한 후 정수로 변환하여 출력해보자")

num = input()
num = int(num)

print(num)



print("변수에 실수값을 저장한 후 변수에 저장되어 있는 값을 그대로 출력해보자.")

num = input()
num = float(num)

print(num)


print("줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.")

num1 = input()
num2 = input()

num1 = int(num1)
num2 = int(num2)

print(num1)
print(num2)

print("줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.")

char1 = input()
char2 = input()

print(char2)
print(char1)

print("실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.")

num = input()

print(num)
print(num)
print(num)

print("공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.")

a, b = input().split()
a=int(a)
b=int(b)
print(a)
print(b)

print("공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.")

a, b = input().split()
print(b, a)

print("정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.")

a = input()
print(a, a, a)

print("24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.")
print("입력 = 3:16 , 출력 = 3:16")

a, b = input().split(':')
print(a, b, sep=':')

print('"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자."')

y, m, d = input().split('.')
print(d, m, y, sep='-')

print("XXXXXX-XXXXXXX \
왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.\
주민번호를 입력받아 형태를 바꿔 출력해보자.")

a,b= input().split('-')
print(a, b, sep='')

print("알파벳과 숫자로 이루어진 단어 1개가 입력된다.\
입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.")

s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

print("6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.")

s = input()
print(s[0:2], s[2:4], s[4:7])
