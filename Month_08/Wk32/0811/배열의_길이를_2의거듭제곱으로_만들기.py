'''
https://school.programmers.co.kr/learn/courses/30/lessons/181857
'''

arr = [1, 2, 3, 4, 5, 6]

def solution(arr):
    count = 0
    answer = arr
    while 1:
        if int(len(arr)) == 2 ** count:
            break
        if int(len(arr)) > 2**count:
            count +=1
        else:
            for i in range(2**count - int(len(arr))):
                answer.append(0)
                break

    return answer

print(solution(arr))
