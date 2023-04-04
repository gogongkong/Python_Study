'''
https://school.programmers.co.kr/learn/courses/30/lessons/60057
'''

def solution(s):
    min_len = len(s)
    # 탐색 범위 : 첫 글자부터 중간까지
    for unit in range(1, (len(s)//2)+1): # 
        previous = s[0:unit]
        result = ""
        count = 1
        # 지정된 탐색 범위 만큼 기존 문자를 슬라이싱 하여 탐색하기
        for i in range(unit, len(s), unit):
            now = s[i:i+unit]

            if now == previous:
                count += 1
            else:
                if count >= 2:
                    result += str(count) + previous
                else:
                    result += previous
                previous = now
                count = 1

        if count >= 2:
            result += str(count) + previous
        else:
            result += previous
        min_len = min(min_len, len(result))

    return min_len




































# def solution(s):
#     min_len = len(s) # 최초 문자열의 길이

#     for unit in range(1, (len(s)//2)+1): # 탐색범위 : 첫글자부터 문자열의 중간까지
#         result = "" # 문자열 저장 변수
#         count = 1
#         previous = s[0:unit] # 탐색 범위, 이전 탐색 범위

#         for idx in range(unit, len(s), unit): # 탐색 인덱스를 탐색 범위만큼 증가 시키고, 이전 탐색범위와 비교하기
#             now = s[idx:idx+unit] # 현재 탐색 단위부터 탐색 범위만큼 증가시키면서 슬라이싱

#             # 현재 탐색 단위가 이전 탐색 단위와 같다면
#             if now == previous:
#                 count += 1
            
#             # 이전과 다르다면
#             else:
#                 if count >= 2:
#                     result += str(count) + previous
#                 else:
#                     result += previous
#                 previous = now
#                 count = 1
#         # 남아있는 문자열을 처리하자
#         if count >= 2:
#             result += str(count) + previous
#         else:
#             result += previous
#         min_len = min(min_len, len(result))
#     return min_len

