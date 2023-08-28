'''
https://school.programmers.co.kr/learn/courses/30/lessons/150370
'''

today1 = "2022.05.19"
todya2 = "2020.01.01"

terms1 = ["A 6", "B 12", "C 3"]
terms2 = ["Z 3", "D 5"]

privacies1 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
privacies2 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]


def solution(today, terms, privacies):
    answer = []

    today = list(map(int, today.split('.')))
    today = today[2] + today[1] * 28 + today[0] * 28 * 12 # 현재 날짜 일단위 합산

    dic = dict()
    for term in terms:
        grade, mounth = term.split()
        dic[grade] = int(mounth) * 28
    
    for i in range(len(privacies)):
        date, cat = privacies[i].split()
        date = list(map(int, date.split('.')))
        date = date[2] + date[1] * 28 + date[0] * 28 * 12

        if date + dic[cat] <= today:
            answer.append(i+1)

    return answer

print(solution(today1, terms1, privacies1))
