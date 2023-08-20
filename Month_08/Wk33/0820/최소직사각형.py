'''
https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''
sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):  
    row = 0
    col = 0

    for x, y in sizes:
        if x < y:
            x, y = y, x
        row = max(row, x)
        col = max(col, y)

    return row * col

print(solution(sizes1))
print(solution(sizes2))
print(solution(sizes3))