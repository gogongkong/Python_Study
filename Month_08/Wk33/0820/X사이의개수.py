'''
https://school.programmers.co.kr/learn/courses/30/lessons/181867
'''

myString = "xabcxdefxghi"

def solution(myString):
    answer = []
    count = 0
    for string in myString:
        if string == "x":
            answer.append(count)
            count = 0
        else:
            count +=1

    answer.append(count)
    
    return answer

print(solution(myString))
