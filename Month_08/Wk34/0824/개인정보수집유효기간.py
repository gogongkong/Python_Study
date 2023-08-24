'''
https://school.programmers.co.kr/learn/courses/30/lessons/150370
'''

today1 = "2022.05.19"
todya2 = "2020.01.01"

terms1 = ["A 6", "B 12", "C 3"]
terms2 = ["Z 3", "D 5"]

privacies1 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
privacies1 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

def solution(today, terms, privacies):
    answer = []


    return answer

result = []

for i in today1.split("."):
    result.append(i)

print(result)

def cal_date(today, date, result):
    result = int(today[2]) - int(date[2])
    today[2] = int(today[2]) - int(date[2])

    if int(today[2]) < 1:
        if int(today[1]) <= 1:
            today[1] = 12
            today[0] = int(today[0]) - 1
            result += 28
        else:
            today[1] = int(today[1]) - 1
            result += 28
        
        today[2] = int(today[2]) + 28
    if int(today[1]) != int(date[1]):
        result += (int(today[1]) - int(date[1])) * 28
        today[1] = int(today[1]) - int(date[1])
        if int(today[1]) < 1:
            today[0] = int(today[0]) -1
            today[1] = int(today[1]) + 12
        
    if int(today[0]) >= int(date[0]):
        result += (int(today[0]) - int(date[0])) * 12 * 28
    
    return result

today = ["2024", "1", "15"]
date = ["2023", "12", "1"]

print(cal_date(today, date, result))