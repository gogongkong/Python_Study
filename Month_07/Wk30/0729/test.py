lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

min_value = 0
for i in lottos:
    if i in win_nums:
        min_value += 1

max_value = min_value + lottos.count(0)
result = [max_value, min_value]

answer = []
for i in result:
    if i == 6:
        answer.append(1)
    elif i == 5:
        answer.append(2)
    elif i == 4:
        answer.append(3)
    elif i == 3:
        answer.append(4)
    elif i == 2:
        answer.append(5)
    else:
        answer.append(6)

print(min_value)
print(max_value)

print(answer)