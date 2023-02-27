# Quiz 1  변수를 이용하여 다음 문장을 출력하시오

# 변수명
#  : station

#  변수값
#   : 사당, 신도림, 인천공항 순서대로 입려 

#   출력 문장
#    : XX 행 열차가 들어오고 있습니다.




# Quiz 2 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.



''' Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
예) http://naver.com
규칙1 : http:// 부분 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver.com
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
                (nav)               (5)             (2)         (!)
예 ) 생성된 비밀번호 : nav52!
'''

url = "http://naver.com"
my = url.replace("http://", "")
my = my[:my.index(".")]
print(my)
pw = str(my[:3]) + str(len(my)) + str(my.count("e")) +"!"
print(pw)

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
user = list(range(1,21))
print(user)
shuffle(user)
print(user)
winner = sample(user, 4)
print(winner)
print(winner[0])
print(winner[1:])



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

count = 0

for i in range(1,21):
    time = randrange(5,51)
    if 5<= time <= 15:
        print("[0] {0}번째 손님 (소요시간: {1}분)".format(i,time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간: {1}분)".format(i,time))

print(count)





# """
# quiz 표준 체중을 구하는 프로그램을 작성하시오

# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째 자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg입니다.
# """

height = 175
gender = "남자"

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    if gender == "여자":
        return height * height * 21

weight = round(std_weight(height/100, gender),2)
print(weight)




#Quiz
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txx', '2주차.txt', .... 와 같이 만듭니다.





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




# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#         출력 메세지 : "잘못된 값을 입력하였습니다."
# 조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#         출력 메세지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
# [코드]

# chicken = 10 # 남은 치킨 수
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#     if order > chicken: # 남은 치킨보다 주문량이 많을 때
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#         waiting += 1 # 대기번호 증가
#         chicken -= order # 주문 수 만큼 남은 치킨 감소




# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오

# 조건: 모듈 파일명은 byme.py 로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브: http://youtube.com
# 이메일: nadocoding@gmail.com









# """정답"""


# url = "http://naver.com"
# my_str = url.replace("http://","")
# my_str = my_str[:my_str.index(".")]
# print(my_str)

# PW = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(PW)





# from random import *
# users = range(1,21)
# users = list(users)
# print(users)
# shuffle(users)
# print(users)
# winners = sample(users,4)
# print(winners)
# print("{0}".format(winners[0]))
# print("{0}".format(winners[1:]))




# from random import *
# cnt = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[O] {0}번쨰 손님 (소요시간 : {1}분".format(i,time))
#         cnt +=1
#     else:
#         print("[ ] {0}번쨰 손님 (소요시간 : {1}분)".format(i,time))
# print("총 탑승 승객 : {}분".format(cnt))



#정답
# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm 남자의 표준 체중은 {1}kg입니다.".format(height,weight))





# class House:
#     #매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
    
#     #매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, \
#             self.completion_year)

# house = []
# house1 = House("강남","아파트","매매", "10억", "2010년")
# house2 = House("마포","오피스텔","전세", "5억", "2007년")
# house3 = House("송파","빌라","월세", "500/50", "2000년")

# house.append(house1)
# house.append(house2)
# house.append(house3)

# print("총 {0}대의 매물이 있습니다.".format(len(house)))
# for i in house:
#     i.show_detail()






# class SoldOutError(Exception):
#     pass

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken:
#             print("재료가 부족합니다.")    
#         elif order <= 0:
#             raise ValueError    
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1
#             chicken -= order

#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break