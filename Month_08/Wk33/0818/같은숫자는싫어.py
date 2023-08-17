'''
https://school.programmers.co.kr/learn/courses/30/lessons/12906
'''
arr= [1,1,3,3,0,1,1]
arr2 = [4,4,4,3,3]
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

    return answer
print(solution(arr))
print(solution(arr2))