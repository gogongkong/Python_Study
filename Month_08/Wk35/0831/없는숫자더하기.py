'''
https://school.programmers.co.kr/learn/courses/30/lessons/86051
'''

numbers1 = [1,2,3,4,6,7,8,0]
numbers2 = [5,8,4,0,6,7,9]

def solution(numbers):
    check = [1,2,3,4,5,6,7,8,9,0]
    result = []
    for i in check:
        if i in numbers:
            result.append(0)
        else:
            result.append(i)
    return sum(result)
print(solution(numbers1))
print(solution(numbers2))