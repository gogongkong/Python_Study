'''
https://school.programmers.co.kr/learn/courses/30/lessons/181890?language=python3
'''

str_list1 = ["u", "u", "l", "r"]
str_list2 = ["l"]
str_list3 = ["q","d"]

def solution(str_list):
    res_l = []
    res_r = []
    if "l" not in str_list and "r" not in str_list:
        return []
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return res_l
        elif i == "r":
            for j in range(i+1, len(str_list)):
                res_r.append(str_list[j])
            return res_r
        res_l.append(str_list[i])


print(solution(str_list1))
print(solution(str_list2))
print(solution(str_list3))
