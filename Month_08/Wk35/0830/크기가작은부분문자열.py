'''
https://school.programmers.co.kr/learn/courses/30/lessons/147355
'''

t1 = "3141592"
t2 = "500220839878"
t3 = "10203"

p1 = "271"
p2 = "7"
p3 = "15"

def solution(t,p):
    answer = 0
    for i in range(len(t)):
        if int(t[i:i+len(p)]) <= int(p) and i <= len(t) - len(p):
            answer += 1
    return answer

print(solution(t1,p1))
print(solution(t2,p2))
print(solution(t3,p3))

