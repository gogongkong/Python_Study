'''
https://school.programmers.co.kr/learn/courses/30/lessons/12954
'''

x, n = -4, 3

def solution(x, n):
    answer = []
    count = int(x)
    answer.append(count)

    for i in range(n-1):
        count += x
        answer.append(count)
    return answer

print(solution(x,n))