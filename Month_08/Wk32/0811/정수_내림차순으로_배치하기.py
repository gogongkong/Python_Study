'''
https://school.programmers.co.kr/learn/courses/30/lessons/12933
'''

n = 118372

def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)

    return int("".join(answer))


print(solution(n))

