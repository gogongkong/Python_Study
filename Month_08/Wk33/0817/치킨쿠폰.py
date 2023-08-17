'''
https://school.programmers.co.kr/learn/courses/30/lessons/120884
'''

# 필요한 변수 정하기
# 전체 치킨의 갯수
# 치킨을 먹은 횟수(=정답)을 담을 변수 = result
# 쿠폰으로 치킨을 먹고 남은 쿠폰의 갯수를 담을 변수 = cupon


chicken = 1081

def solution(chicken):
    result = chicken // 10
    cupon = (chicken // 10) + (chicken % 10)

    while cupon // 10 != 0:
        result += cupon // 10
        cupon = (cupon // 10) + (cupon % 10)

    return result

solution(chicken)