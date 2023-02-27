
#실수형 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

#문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

#boolean 자료형
#참 / 거짓을 의미
print(5>10)     # 기댓값 : False
print(5<10)     # 기댓값 : True
print(True)     # 기댓값 : True
print(False)    # 기댓값 : False
print(not True) # not True --> True의 반대는? --> False
print(not False)# not False --> False의 반대는? --> True
print(not (5>10))# False의 반대 --> Ture 

#변수
#애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3


print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이" # 중간에 변수를 변경
print(name+ "는 " + str(age) +  "살이며," +hobby+"을 아주 좋아해요")
print(name,"는", age,"살이며," ,hobby,"을 아주 좋아해요") # , 는 띄어쓰기가 하나씩 포함됨
print(name+ "는 어른일까요? " +str(is_adult))

''' 이렇게 하면
여러줄의 문장을
주석 처리를 할 수 있다
'''
# 드래그 하고 컨트롤 + 슬러시 하면 범위 주석


# quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명
#  : station

#  변수값
#   : 사당, 신도림, 인천공항 순서대로 입려 

#   출력 문장
#    : XX 행 열차가 들어오고 있습니다.

station = "인천"

print(station+ "행 열차가 들어오고 있습니다.")

station = "신도림"

print(station+ "행 열차가 들어오고 있습니다.")

station = "인천공항"

print(station+ "행 열차가 들어오고 있습니다.")




###############연산자###############

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2
print(2**3) #2^3 = 8
print(5%3) # 5나누기 3의 나머지 = 2
print(10%3) #1
print(5//3) #몫 구하기 =1
print(10//3) #3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True
print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) #같지 않다의 연산자 = True
print(not(1 != 3)) # False
print((3 > 0 ) and (3 < 5)) # True
print((3 > 0) & (3 < 5) ) # True (& <-- and와 동일)

print((3 > 0) or ( 3 < 5)) #둘중 하나만 True
print((3 > 0 ) | (3 > 5)) #True ( | <-- or와 동일)
print(5 > 4 > 3) # True
print(5 > 4 > 7) # False


##############간단한 수식############
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4
print(number)

number = number + 2
print(number) # 16

number += 2 # 18
print(number)

number *= 2 # 36
print(number)

number /= 2 # 18
print(number)

number -= 2 # 16
print(number)

number %= 5 #1
print(number)

########## 숫자처리 함수 ###########
print(abs(-5)) # 5 절대값
print(pow(4, 2)) # 4의 2승 = 16
print(max(5, 12)) # 최댓값 = 12
print(min(5, 12)) # 최솟값 = 5
print(round(3.14)) # 반올림 = 3
print(round(4.99)) # 5

from math import * #math라는 library 안의 모든것을 이용하겠다
print(floor(4.99)) # 내림 = 4
print(ceil(3.14)) # 올림 = 4
print(sqrt(16)) # 제곱근 = 4


########## 랜덤 함수 #############

#난수 무작위로 숫자를 뽑아줌

from random import *

# print(random()) # 0.0 ~ 1.0이하 사이의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0이하 사이의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10이하 사이의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10이하 사이의 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45미만 사이의 임의의 값 생성

print(randrange(1, 46)) # 1 ~ 46미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성

#Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

#내 풀이
from random import *
print("오프라인 스터디 모임 날짜는 매월" + str(randint(4, 28)) + "일로 선정 되었습니다.")

# 유튜브 풀이
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정 되었습니다.")


############# 문자열 ############

sentence = '나는 소년 입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)

sentence = """나는 소년이고
파이썬은 쉬워요
"""

print("sentence3")


###########슬라이싱##############

jumin = "931221-1234567"

print("성별 : " +jumin[7])
print("년도 : " +jumin[0:2]) # 0:2 --> 0부터 2 직전까지 (0,1)
print("월 : " +jumin[2:4])
print("일 : " +jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # :6 --> 처음부터 6직전까지

print("뒤 7자리 : " +jumin[7:14])
print("뒤 7자리 : " +jumin[7:]) # 7: --> 7번째부터 끝까지
print("뒤 7자리 (뒤에서부터) : " +jumin[-7:]) # 맨뒤에서 7번째부터 끝까지

##########문자열 처리 함수 ######## 

python = "Python is Amazing"
print(python.lower()) # .lower() --> 소문자로 변환
print(python.upper()) # .upper() -->대문자로 변환
print(python[0].isupper()) #0번째 문자가 대문자 인지?
print(len(python)) #길이를 세주는 함수 len(변수)
print(python.replace("Python", "Java")) #.replace() --> 문자 변경

index = python.index("n") # index() 괄호 안의 문자가 몇번째에 위치해있는지?
print(index) #5
index = python.index("n", index + 1) #index +1 번째의 n 즉 2번쨰 n이 몇번째인가?
print(index)

print(python.find("n")) # find는 index같은 함수임
print(python.find("Java")) #원하는 값이 없으면 -1을 반환하는 함수 find()
# print(python.index("Java")) index는 없는값을 넣으면 그냥 에러를 냄
# 에러가 있으면 그 뒤에 코드는 출력이 안됨. 그 차이를 알자

print(python.count("n")) #count함수 --> 원하는 값이 몇번 등장하는지 ->2번

####################문자열 포맷#############

print("a" +"b")
print("a","b")

#방법 1
print("나는 %d살 입니다." %20) # %d --> 문자 뒤 %뒤의 값을 %d에 넣음 %d는 항상 정수값만 들어감
print("나는 %s를 좋아해요. " %"파이썬") # %s --> 문자열값String(str)
print("Apple 은 %c로 시작해요" %"A") # %c --> 한글자만 받음

# 참고 %s는 정수건 문자건 문자열이건 다 받음
print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요" % ("파란","빨간"))

#방법 2
print("나는 {}살입니다.".format(20)) #나는 20살입니다.
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간")) #나는 파란색과 빨간색을 좋아해요
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간")) #나는 파란색과 빨간색을 좋아해요
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간")) #나는 빨간색과 파란색을 좋아해요

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간")) #나는 20살이며, 빨간색을 좋아해요
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20)) #나는 20살이며, 빨간색을 좋아해요

# 방법 4 v3.6이상
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") #f 붙이면 실제 변수에서 그대로 가져다가 쓸 수 있음
#나는 20살이며, 빨간색을 좋아해요


########## 탈출문자 ##############

print("백문이 불여일견 백견이 불여일타")
print("백문이 불여일견\n 백견이 불여일타") #\n 줄바꿈

# 원하는 출력 문자 : 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.") # \ <-- 따옴표같은 문법에 문제 될 수 있는거 출력시켜줌

# \\ : 문장 내에서 하나의 \ 로 인식
print("D:\\PythonWorkSpace\\drobox")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple

#\b : 백스페이스 (한글자 삭제)
print("Redd\b Apple")

#\t : 탭(Tab)
print("Red\tApple")

''' Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1 : http:// 부분 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver.com
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                (nav)               (5)             (2)         (!)
예 ) 생성된 비밀번호 : nav52!
'''
url = "http://naver.com"
my_str = url.replace("http://", "")
print(my_str) #naver.com
my_str = my_str[:my_str.index(".")]
print(my_str) # naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

########### 리스트 ###########

''' 순서를 가지는 객체의 집합'''

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway) #[10, 20, 30]

subway = ["유재석", "조세호", "박명수"] #['유재석', '조세호', '박명수']
print(subway)

# 조세호씨가 몇번째 칸에 타고있는가"
print(subway.index("조세호")) # 1

#다음 정류장에서 하하가 탔다
subway.append("하하")
print(subway) #['유재석', '조세호', '박명수', '하하']

#정형돈씨를 유재석과 조세호 사이에 넣는다.
subway.insert(1, "정형돈")
print(subway) #['유재석', '정형돈', '조세호', '박명수', '하하']

#뒤에서 부터 하나씩 빼보기
print(subway.pop()) #하하
print(subway) #['유재석', '정형돈', '조세호', '박명수']
# print(subway.pop()) #박명수
# print(subway) #['유재석', '정형돈', '조세호']
# print(subway.pop()) #조세호
# print(subway) #['유재석', '정형돈']
# print(subway.pop()) #정형돈
# print(subway) #['유재석']


#같은 이름의 사람이 몇명 있는지 확인하기
subway.append("유재석")
print(subway) #['유재석', '정형돈', '조세호', '박명수', '유재석']
print(subway.count("유재석")) #2

#정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list) #[1, 2, 3, 4, 5]

#뒤집기도 가능
num_list.reverse()
print(num_list) #[5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) #[]

# 자료형에 구애 받지 않고 섞어 사용이 가능
mix_list = ["조세호", 20, True]
print(mix_list) #['조세호', 20, True]

#리스트 확장 가능
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list) #[5, 2, 4, 3, 1, '조세호', 20, True]


########## 사전 ##########

cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) #김태호

print(cabinet.get(3)) # 유재석
#print(cabinet[5]) <-- 5번은 없기 때문에 에러를 반환하여 이후 코드를 실행하지 않음
print(cabinet.get(5)) # None --> 없어도 None을 출력하여 이후 코드 실행하게 함
print(cabinet.get(5, "사용가능")) # 사용가능 --> 5가 없으면 뒤에 글자를 출력하게 하는것

print(3 in cabinet) # in : 3이 cabinet 안에 있다면 True 출력
print(5 in cabinet) # False

#  정수가 아닌 문자도 가능
cabinet = { "A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"]) #유재석
print(cabinet["B-100"]) #김태호
# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet) #{'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"] # A-3은 삭제
print(cabinet) #{'B-100': '김태호', 'C-20': '조세호'}

#key 들만 출력
print(cabinet.keys()) #dict_keys(['B-100', 'C-20'])

#Value 들만 출력
print(cabinet.values()) #dict_values(['김태호', '조세호'])

#key / Value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])


#폐점  전체삭제
cabinet.clear()
print(cabinet) # {}


#################튜플 #################

#튜플은 리스트와 다르게 수정이 불가능 하지만 속도가 빠르다

menu = ("돈까스", "치즈까스")
print(menu[0]) #돈까스
print(menu[1]) # 치즈까스

#menu.add("생선까스") 에러뜸 add는 안됨

name = "김종국"
age = "20"
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)




############ 세트 #################
# 세트 (set)
# 중복이 안되고, 순서가 없음
my_set = {1,2,3,3,3,3}
print(my_set) # {1, 2, 3} <-- 중복이 안되니까 3이 한번만
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) #자바 파이선 둘다 유재석은 중복됨
#교집함 = 자바와 파이썬 모두 가능한 사람 = 유재석 

print(java & python) #{'유재석'}
print(java.intersection(python))#{'유재석'}

#합집합 (java나 python 둘중 하나만 할 수 있는사람)
print(java | python) #{'양세형', '유재석', '박명수', '김태호'}
print(java.union(python)) #{'양세형', '유재석', '박명수', '김태호'}

#차집합 (자바는 할 수 있지만 파이선은 못하는애들)
print(java-python) #{'김태호', '양세형'}
print(java.difference(python)) #{'김태호', '양세형'}

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) #{'박명수', '김태호', '유재석'}

#java를 까먹은사람
java.remove("김태호")
print(java) #{'양세형', '유재석'}


############자료구조의 변경###########
# 자료 구조의 변경
#커피숍
menu = {"커피", "우유", "주스"}
print(menu) #{"커피", "우유", "주스"}
print(menu, type(menu)) #{'우유', '주스', '커피'} <class 'set'> 세트 타입의 변수

menu = list(menu)
print(menu, type(menu)) # ['커피', '우유', '주스'] <class 'list'> 리스트로 변경된 menu

menu = tuple(menu)
print(menu, type(menu)) #('우유', '커피', '주스') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) #<class 'set'>


# Quiz ) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20이라고 가정
# 조건 2 : 댓글 내용과 상관 없이 무작위 로 추첨 하되 중복 불가
# 조건 3 : random 모듈의 shuffle과 sample을 활용

# (출력 예제)
#  -- 당첨자 발표 --
#  치킨 당첨자 : 1
#  커피 당첨자 : [2, 3, 4]
#  -- 축하합니다. --

#  (활용 예제)
#  from random import *
#  lst = [1,2,3,4,5]
#  print(lst)
#  shuffle(lst)
#  print(lst)
#  print(shuffle(lst, 1))

from random import *
users = range(1,21) #1부터 21 직전까지
users = list(users)
print(users)

shuffle(users)
print(users)
winners = sample(users, 4) #한명은 치킨 3명은 커피


print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다.--")

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

############### if ####################
# if 조건:
#     실행 명령문
# elif 조건:
#     실행 명령문
# else:
#     실행 명령문
weather ="비" #input("오늘 날씨는 어때요? : ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요.")

temp = 11 #int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요 나가지 말아요")
elif 10<= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 < temp < 10:
    print("외투를 챙기세요")
else:
    print("너무추우니 나가지 말아요")

############# for #############
#반복문

for waitting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waitting_no))
#randrange()
for waitting_no in range(1,6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waitting_no))

starbucks = ["아이언맨", "토르", "아이엠그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비 되었습니다.",format(customer))

############## while ##############
#반복문
#while (조건):

customer = "토르"
index = 5

while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. {1}번 호출하였습니다.".format(customer,index))
#     index += 1

customer = "토르"
person = "unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = "토르" #input("이름이 어떻게 되세요? : ")

############ continue와 break ##########
absent = [2,5] #결석
no_book = [7] #책이 없음
for student in range(1,11):
    if student in absent:
     continue
    elif student in no_book:
        print("오늘 수업 없음 {}은 교무실로".format(student))
        break
    print("{}, 책을 읽어봐".format(student))

## 책이 없는 번호가 나오면 마지막에 한번에 교무실로 보내기
absent = [2,5] #결석
no_book = [7,6] #책이 없음
stu = ""
stu = set(stu)
for student in range(1,11):
    if student in absent:
     continue
    elif student in no_book:
        print("{}은 책이 없구나?".format(student))
        stu.add(student)
    print("{}, 책을 읽어봐".format(student))
print("책이 없는 {}는 교무실로 와라".format(stu))

########## 한줄 for ############
#출석번호 1 2 3 4 앞에 100을 붙이기로 함 --> 101 102 103 104
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [len(i) for i in student]
print(student)

#학생 이름을 대문자로 변환
student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student]
print(student)

# Quiz) 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해짐
# 조건2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

from random import *
cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[0] {0}번째 손님, 소요시간 : {1}분".format(i,time))
        cnt +=1
    else:
        print("[ ] {0}번째 손님 소요시간 : {1}분".format(i,time))
print("총 탑승 승객 {}분".format(cnt))

############ 함수 ##########
def open_account():
    print("새로운 계좌가 생성 되었습니다.")

open_account()
######### 전달값과 반환값#########
def deposit(balance, money): # 입금 
    print("입금이 완료 되었습니다, 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료 되지 않았습니다, 잔액은 {0}원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금 수수료
    commission = 100 #수수로 100원
    return commission, balance - money - commission

balance = 0 #잔액
balance = deposit(balance, 1000)
print(balance)

# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance,500)
print("수수로는 {0}원이며, 잔액은{1}원입니다.".format(commission, balance))

######### 기본값 ##########
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 24, "자바")

#같은 학교 같은 학년 같은 반 같은 수업 - 이름 다르고 나이와 언어는 같은거
#이때 사용하는것이 기본갓
def profile1(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
        .format(name, age, main_lang))
profile1("유재석")
profile1("김태호")
profile1("유급생", 18, "파이썬, 자바")

############ 키워드값 ##########

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=20, name="김태호")
# 키워드에 맞춰서 입력을 해주면 순서 뒤바뀌어도 사용가능

############ 가변 인자 ##########
def profile2(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0} \t나이 : {1}".format(name, age), end=" ")
# end " " print문 끝나고 줄바꿈 없이 이어서 나감
    print(lang1, lang2, lang3, lang4, lang5)
profile2("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile2("김태호", 24, "Kotlin", "Swift", "","","")
#매번 빈칸 넣는다던지 lang6까지 넣어야 할수도 있는데 그떄 쓰는 것이 가변인자

def profile3(name, age, *language):
    print("이름 : {0} \t나이 : {1}".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile3("유재석", 20, "Python", "Java", "C", "C++", "C#","자바스크립트")
profile3("김태호", 24, "Kotlin", "Swift")

########### 지역변수와 전역 변수 ############
# 지역 변수 : 함수 내에서만 사용가능 함수가 호출이 될때 사용하고 호출이 끝나면 사라짐
# 전역 변수 : 모든 공간에서 프로그램 내 어디서든 사용 가능

gun = 10

def checkpoint(soldiers): # 경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무를 나감
print("남은 총 : {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은 총 : 18
# 남은 총 : 10 --> 함수 내에서 선언된 gun만 사용하고 사라지기때문에 "지역변수"

def checkpoint2(soldiers): # 경계근무
    global gun # gloabal = 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint2(2) # 2명이 경계근무를 나감
print("남은 총 : {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8

"""일반적으로 전역 변수를 많이 쓰게 되면 코드 관리가 어려워 권장되는 방법은 아님 가급적 파라미터로 사용하고 반환값을 받아 사용"""

def check_point_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
#return을 함으로서 gun이라는 바뀌어진 값을 외부로 보낼 수 있음

print("전체 총 : {0}".format(gun))
gun = check_point_return(gun, 2)
print("남은 총 : {0}".format(gun))


"""
quiz 표준 체중을 구하는 프로그램을 작성하시오

*표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) x 키(m) x 22
여자 : 키(m) x 키(m) x 21

조건1 : 표준 체중은 별도의 함수 내에서 계산
    * 함수명 : std_weight
    * 전달값 : 키(height), 성별(gender)
조건2 : 표준 체중은 소수점 둘째 자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg입니다.
"""
# 내풀이
def my_std_weight(height, gender):
    height = height * 0.01
    man_weight = height * height * 22
    woman_weight = height * height * 21
    if gender == "man":
        print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height*100,str(round(man_weight,2))))
    elif gender =="woman":
        print("키 {0}cm 여자의 표준 체중은 {1}kg입니다.".format(height*100,str(round(woman_weight,2))))
    return height, gender
my_std_weight(175, "man")

#정답
def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height,weight))


###############표준입출력##############
print("python","java") #python java
print("python"+"java") #pythonjava
print("python", "java", sep=",") #python,java
print("python", "java","Javascript",sep=" vs ") #python vs java vs Javascript
print("python", "java", sep=".", end="?") #python.java?무엇이 더 재밌을까요?
print("무엇이 더 재밌을까요?") #python.java?무엇이 더 재밌을까요?

# import sys
# print("python","java", file = sys.stdout) # 표준 출력으로 찍히는것
# print("python","java", file = sys.stderr) # 표준 에러로 찍히는것

#시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items(): #.items --> 변수 안에 키(subject)와 밸류(score)를 쌍으로 튜플로 보내줌.
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # .ljust -> 왼쪽으로 8칸 공간확보하여 정렬 rjust --> 오른쪽
# 수학 0
# 영어 50
# 코딩 100

### 줄 정렬을 하고 싶을때


#은행 대기 순번표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) # zfill == 0을 채우는것


###표준입력######
# answer = input("아무값이나 입력하세요 : ")
# print(type(answer)) # input으로 값을 받게되면 항상 문자의 형태로 받게됨
# print("입력하신 값은 " + answer + "입니다.")


##########다양한 출력 포멧 ##############
# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) #       500

# 양수일 땐 +표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) #      +500
print("{0: >+10}".format(-500)) #      -500

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500)) #+500______

# 3자리 마다 콤마(,)찍어주기
print("{0:,}".format(100000000)) #100,000,000
# 3자리 마다 콤마(,)찍어주기, +- 부호붙이기
print("{0:+,}".format(100000000)) #+100,000,000
print("{0:+,}".format(-100000000)) #-100,000,000

# 3자리 마다 콤마(,) 찍어주고, 부호도 붙이고. 자리수도 확보하기
# 돈이 많으면 기분이 좋으니까 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(10000000000000000)) #+10,000,000,000,000,000^^^^^^^
#소수점 출력
print("{0:f}".format(5/3)) #1.666667
#소수점을 특정 자리수까지만 표시
print("{0:.2f}".format(5/3)) #1.67 (3째 자리에서 반올림)


######## 파일 입출력 ######### 
#파이썬을 이용해서 컴퓨터 내 파일을 불러 올 수 도 있고 원하는 내용을 쓸 수 도 있다.

# score_file = open("score.txt", "w", encoding="utf8") #open(파일명, 목적 =읽기 or 쓰기, 인코딩 정보) utf8 = 한글--> 추천
# print("수학 : 0", file=score_file) 
# print("영어 : 50", file=score_file)
# score_file.close() #파일을 열었으면(.open) 닫아야 합니다.(,close)

# score_file = open("score.txt", "a", encoding="utf8") # w는 다시 사용하면 덮어쓰기지만 a는 이어쓰기(append)
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") #.write로 썻을때는 줄바꿈이 기본으로 적용 되지 않기 때문에 따로 \n을 사용해줘야함
# score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r은 읽기
print(score_file.read()) # 그냥 .read는 모두 읽기
score_file.close()

print("\n\n\n\n\n\n\n\n\n")

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # readline = 한줄만 읽어오고 나서 커서를 다음줄로 이동
print(score_file.readline(), end="")
print(score_file.readline())
print(score_file.readline())
score_file.close()

print("\n\n\n\n\n\n\n\n\n")

score_file = open("score.txt", "r", encoding="utf8")
while True: # 파일의 내용이 몇줄인지 모를때 
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

print("\n\n\n\n\n\n\n\n\n")

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()# 모든 라인을 가져와서  list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()



############# Pickle ########## 
# 프로그램상에서 사용하고 있는 데이터를 파일형태로 저장하는것 누군가에게 주면 그사람도 pickle 형태로 읽어야함
import pickle
# profile_file = open("profile.pickle", "wb",) #wb할대 b는 binery를 의미함 pickle을 사용할땐 언제나 b를 써줘야함 pickle에서는 따로 인코딩 설정 X
# profile = {"이름" : "박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)# profile에 있는 정보를 file에 저장 
# profile_file.close()

profile_file = open("profile.pickle", "rb",)
profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()


################ with #############

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
#with문을 사용할땐 close 사용을 하지 않아도 자동으로 탈출시켜줌

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
# with를 쓰면 줄수도 적고 매번 close할 필요가 없음


#Quiz
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txx', '2주차.txt', .... 와 같이 만듭니다.
 

#내풀이
# for week in range(1,51):
#     with open("{0}주차.txt".format(week), "w", encoding="utf8") as week_file:
#         week_file.write(" - {0}주차 주간보고 - \n".format(week))
#         week_file.write("부서 : \n")
#         week_file.write("이름 : \n")
#         week_file.write("업무 요약 : \n")
#     i += i

#해답
# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(" - {0}주차 주간보고 - \n".format(i))
#         report_file.write("부서 : \n")
#         report_file.write("이름 : \n")
#         report_file.write("업무 요약 : \n")

print("\n\n\n\n\n\n\n\n\n")

########## 클래스 ###############

# 마린 : 공격유닛 , 군인 , 총을 쏠 수 있음
# name = "마린" #유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# #탱크 : 공격유닛, 탱크, 포를 쏠 수 있는데, 일반모드와 시즈모드가 있음
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시방향", damage)
# attack(tank_name, "1시방향", tank_damage)
# attack(tank2_name, "1시방향", tank2_damage)

#이게 뭔 개뻘짓인가 싶으니까 있는것이 클래스다
# 붕어빵틀 같은 개념 = 일반적으로 서로 연관이 있는 변수와 함수의 집합
print("\n\n\n\n\n\n\n\n\n")


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

############ __init__ #############
# 파이썬에서 사용되는 생성자 / 클래스로부터 만들어지는 객체를 생성할때 안에 필요한 변수들을 충족해야 생성됨
# ex : Unit 클래스에서 마린만 적는것 처럼 hp나 damage를 안적으면 안됨(에러 발생)

########## 멤버변수 #############
# 멤버변수 = self.name / self.hp / self.damage
# 즉 클래스 내에서 정의 된 변수고 그 변수를 가지고 우리가 초기화 및 사용이 가능 

# 레이스 : 공중유닛 , 비행기, 클로킹(투명)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 클래스.변수명으로 외부에서 사용도 가능

# 마인트 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name)) # --> 클로킹이라는 변수는 클래스에없지만 외부에서 추가함

# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
# 에러남 == 기존에 확장한 변수는 해당 변수에만 적용됨을 의미



############# 메소드 ##############
from random import *

#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("{0} : {1} 방향으로 이동 합니다. [속도 {2}]".format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

########## 상속 ###########
#클래스끼리 겹치는 부분이 있을 때 사용 가능
# ex : AttackUnit과 Unit은 self.name, self.hp가 겹친다
#사용법 :   AttackUnit(Unit) --> 클래스명(상속받을 클래스)
#           Unit.__init__(self,name, hp) --> 상속받을 클래스.__init__(self.상속받을 변수)와 같이 사용



############ 다중 상속 ###########
# 상속을 받는데 여러개의 부모클래스에게 상속을 받음

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self,name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
        # self.name/self.damage = __init__의 name과 damage를 쓰겟다는것
        # location = attack 안에 잇는것을 그대로 사용하겠다.

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    #스팀팩 : 일정시간 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜 더 높은 공격을 함, 이동 불가
    seize_developed = False # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드가 아닐때 -> 시즈모드
        if self.set_seize_mode == False:
            print("{0} : 시즈모드 해제 합니다.".format(self.name))
            self.damage /=2
            self.seize_mode == True
        # 현재 시즈모드일때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드로 설정 합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode == False

#날 수 잇는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self,name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

#레이스
class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹모드 해제상태

    def clocking(self):
        if self.clocked == True: #클로킹 해제
            print("{0} : 클로킹 모드 해제 합니다.".format(self.name))
            self.clocked = False
        else: # 클로킹 모드 해제 --> 모드 설정
            print("{0} : 클로킹 모드 설정 합니다.".format(self.name))
            self.clocked = True


####### 메소드 오버라이딩 #######
# 부모클래스를 정의한 메소드 말고 자식클래스에서 정의한 메소드를 쓰고 싶을떄
# 메소드를 새롭게 정의하여 사용 할 수 있음

#벌쳐 : 지상유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀 크루저 : 공중유닛, 체력도 좋고, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시 방향")
# # battlecruiser.fly(battlecruiser.name, "9시") 
# # 문제점 : 지상유닛은 move함수 공중 유닛은 fly함수 --> 매번 지상인지 공중인지 확인해야함
# battlecruiser.move("9시")

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
########### pass ###########

#건물을 만든다
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
        #pass # 에러가 뜨지만 일단 넘어간다는 뜻

# 서플라이 : 건물, 1개 마다 유닛 8        
# # supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()


############# super #############

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # super를 쓸때는 __init__을 써줘야 하지만 self는 안써도 됨
#         self.location = location
#문제는 다중상속에서 발생 
#맨처음 상속받는 클래스에 대해서만 __init__함수가 호출이 된다. --> prctice_class.py참조


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

#게임 시작
game_start()

#마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 2기 생성
t1 = Tank()
t2 = Tank()

#레이스 1기 생성
w1 = wraith()

#유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료 되었습니다.")

#공격 모드 준비(마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):#isinatance : 지금 만들어진 객체가 어떤 class의 인스턴스인지 확인하는것
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, wraith):
        unit.clocking()
    

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) #공격은 랜덤으로 받음

# 게임 종료
game_over()


# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         pass
    
#     #매물 정보 표시
#     def show_detail(self):
#         pass

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, \
            self.completion_year)

house = []
house1 = House("강남","아파트","매매", "10억", "2010년")
house2 = House("마포","오피스텔","전세", "5억", "2007년")
house3 = House("송파","빌라","월세", "500/50", "2000년")

house.append(house1)
house.append(house2)
house.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(house)))
for i in house:
    i.show_detail()

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

########## 예외 처리 #############
#에러에 대한 예외 처리
#사용법
#try:
#   코드 ... 
#except 에러커즈:
#   해당 에러커즈가 발생시 행동 입력 (ex print("에러발생!"))
#except 에러코드 as err:
#   print(err) err : 에러 문장을 그대로 출력 / Exception :  
#except만 적었을때 그냥 에러만 발생하면 바로 아랫문장 실행


# try:
#     print("나누기 전용 계산기 입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요: ")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2} ".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력 하였습니다!")
# except ZeroDivisionError as err: 
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생 하였습니다.")
#     print(err)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

########## 에러 발생시키기 #########

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise ValueError #해당 조건을 만족시 ValueError로 에러를 발생시킴 (raise)
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력 하였습니다. 한자리 숫자만 입력 하세요")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

############ 사용자 정의 예외 처리 ###########

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력 하였습니다. 한자리 숫자만 입력 하세요")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력 하세요")
#     print(err)

############# finally #############
# finally는 예외 처리 중에서 정상적으로 수행이 되던 안되던 무조건 처리되는 구문
#try문의 제일 마지막줄에 입력
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기 입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >=10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력 하였습니다. 한자리 숫자만 입력 하세요")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력 하세요")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")



# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다."

# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."






#[코드]
# chicken = 10 # 남은 치킨 수
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1 # 대기번호 증가
#             chicken -= order # 주문 수 만큼 남은 치킨 감소
        
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력 하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 장사 안합니다.")
#         break



############ 모듈 ############
#필요한 것들만 모아둔 함수 정의나 클래스 파이썬 문장들이 있음(확장자 .py)
#모듈은 내가 쓰려는 모듈과 같은 경로에 있거나 파이썬 라이브러리가 모여있는 폴더에 있어야 사용 가능

import theater_module

theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
theater_module.price_mornig(4) #4명이서 조조 할인 영화 보러 갔을 때 가격
theater_module.price_soldier(5) #5명의 군인이 영화 보러 갔을 때 가격

print("\n\n\n\n\n\n\n\n\n")

import theater_module as mv # as mv --> as 뒤에 붙인걸로(mv)로 간편히 붙일 수 있음
mv.price(3)
mv.price_mornig(4)
mv.price_soldier(5)

print("\n\n\n\n\n\n\n\n\n")

from theater_module import* #as mv 이런거 없이 더 간편하게
price(3)
price_mornig(4)
price_soldier(5)

print("\n\n\n\n\n\n\n\n\n")

from theater_module import price, price_mornig #해당 모듈에서 원하는 함수만 사용 가능

price(5)
price_mornig(6)

print("\n\n\n\n\n\n\n\n\n")

from theater_module import price_soldier as sprice
sprice(5)


########## 패키지 ##########
#모듈들을 모아놓은 집합

# import travel.thailand #import 맨뒤에는 모듈이나 패키지만 사용 가능 / 함수나 클래스는 사용 불가능 -->오류뜸
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage #이거처럼 from ~ import에서는 클래스를 사용 가능
# trip_to = ThailandPackage()
# trip_to.detail()


# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

print("\n\n\n\n\n\n\n\n\n")

########## __all__ ###########
from travel import * # 그냥 쓰면 오류 발생 --> 공개 범위 설정 필요 --> __init__.py파일 참조
trip_to = thailand.ThailandPackage()
trip_to.detail()

print("\n\n\n\n\n\n\n\n\n")

########## 모듈 직접 실행 ##########
#Thailand.py 참조

######### 패키지 모듈 위치 #########
import inspect
from travel import *
import random
print(inspect.getfile(random)) #C:\Python311\Lib\random.py
print(inspect.getfile(thailand)) #c:\Users\User\Desktop\PythonWorkSpace\travel\thailand.py



########### pip install ###########
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
#pip 에 대한 업데이트(업그레이드)가 필요하다
# = pip install --upgrade 패키지명 
#pip 삭제
# = pip uninstall 패키지명

######### 내장 함수 ##########
# 내장함수란 이미 내장되어 있는 함수이기 때문에 따로 import 없이 사용 가능 
# ex : input 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어 입니다.".format(language))

#dir : 어떤 객체를 넘겨 줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random #외장함수
print(dir()) # import된 것들을 보여줌

print(dir(random)) #random 모듈 내에서 쓸 수 있는것들을 보여줌


print("\n\n\n\n\n\n\n\n\n")

lst = [1, 2, 3]
print(dir(lst)) #리스트에서 쓸 수 있는 내용들을 볼 수 있음

print("\n\n\n\n\n\n\n\n\n")

name = "Jim"
print(dir(name))

# https://docs.python.org/ko/3/library/functions.html (구글 검색 : list of python builtins)
# 위 링크에서 내장 함수들을 모두 볼 수 있음

print("\n\n\n\n\n\n\n\n\n")

######## 외장 함수 ##########
# url : https://docs.python.org/ko/3/py-modindex.html
# 검색 : list of python modules

#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 : dir)
import glob
print(glob.glob("*.py")) #확장자가 py인 모든 파일 

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 표시 #C:\Users\User\Desktop\PythonWorkSpace

folder = "sample_dir"
if os.path.exists(folder): #sample_dir 이라는 폴더가 있으면 아래 코드 실행
    print("이미 존재하는 폴더 입니다.")
    os.rmdir(folder)
    print("smaple_dir 폴더를 삭제 하였습니다.")
else:
    os.makedirs(folder) # 폴더 생성
    print("폴더를 생성합니다.")

print(os.listdir())

print("\n\n\n\n\n\n\n\n\n")

#time : 시간 관련 함수
import time 
print(time.localtime())
print(time.strftime("%y-%m-%d %H:%M:%S"))

print("\n\n\n\n\n\n\n\n\n")

import datetime
print("오늘 날짜는 ", datetime.date.today())

#timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) #100일 저장
print("오늘부터 100일 후는", today + td)


print("\n\n\n\n\n\n\n\n\n")

# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건: 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브: http://youtube.com
# 이메일: nadocoding@gmail.com

import byme
byme.sign()


