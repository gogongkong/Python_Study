'''
https://school.programmers.co.kr/learn/courses/30/lessons/181890?language=python3
'''

str_list1 = ["u", "u", "l", "r"]
str_list2 = ["l"]
str_list3 = ["q","d"]

def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == "l":
            return str_list[:i]
        elif str_list[i] == "r":
            return str_list[i+1:]
    return []

# enumerate 이용
def solution2(str_list):
    for i, data in enumerate(str_list):
        if data == "l":
            return str_list[:i]
        elif data == "r":
            return str_list[i+1:]
    return []


print(solution(str_list1))
print(solution(str_list2))
print(solution(str_list3))

print(solution2(str_list1))
print(solution2(str_list2))
print(solution2(str_list3))
