'''
https://school.programmers.co.kr/learn/courses/30/lessons/120912
'''

array1 = [7, 77, 17]
array2 = [10, 29]


def solution(array):
    answer = 0
    for arr in array:
        for check in str(arr):
            if check == "7":
                answer += 1
    return answer

print(solution(array1))
print(solution(array2))


# Pythonic
def solution2(array):
    return str(array).count("7")

print(solution2(array1))
print(solution2(array2))