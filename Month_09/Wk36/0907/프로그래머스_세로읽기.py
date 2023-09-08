'''
https://school.programmers.co.kr/learn/courses/30/lessons/181904
'''
my_string1 = "ihrhbakrfpndopljhygc"
my_string2 = "programmers"
m1 = 4
m2 = 1
c1 = 2
c2 = 1

def solution(my_string, m, c):
    answer = ''
    count= 0
    answer += my_string[c-1]
    for i in range(c,len(my_string)):
        count += 1
        if count == m:
            answer += my_string[i]
            count = 0
    return answer 

print(solution(my_string1, m1, c1))
print(solution(my_string2, m2, c2))