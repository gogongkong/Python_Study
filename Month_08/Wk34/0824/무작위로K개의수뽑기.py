'''
https://school.programmers.co.kr/learn/courses/30/lessons/181858
'''


arr1 = [0, 1, 1, 2, 2, 3]
arr2 = [0, 1, 1, 1, 1]

k1 = 3
k2 = 4

def solution(arr, k):
    answer = []

    for arrs in arr:
        if arrs not in answer:
            if len(answer) < k:
                answer.append(arrs)
            elif len(answer) == k:
                break
    if len(answer) == k:
        return answer
    else:
        for _ in range(k - len(answer)):
            answer.append(-1)
        return answer
    

print(solution(arr1, k1))
print(solution(arr2, k2))