'''
https://school.programmers.co.kr/learn/courses/30/lessons/176963
'''

def solution(name, yearning, photo):
    result = 0
    answer = []
    data = {n:y for n,y in zip(name, yearning)}
    for picture in photo:
        for pic in picture:
            if pic in data:
                result += data[pic]
        answer.append(result)
        result = 0
    return answer