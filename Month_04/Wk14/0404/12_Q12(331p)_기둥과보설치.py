'''
https://school.programmers.co.kr/learn/courses/30/lessons/60061?language=python3
'''

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝부분 위' 혹은 '다른 기둥 위' 라면 정상
            if y == 0 or [x-1, y,1] in answer or [x,y,1] in answer or[x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1: # 설치된것이 '보' 인경우
            # '한쪽 끝부분이 기둥위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결' 이라면 정상
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame): 
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x,y,stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x,y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1:
            answer.append([x,y,stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x,y,stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환