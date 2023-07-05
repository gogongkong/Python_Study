'''
https://www.acmicpc.net/problem/1541
'''

data = input().split("-")

result = 0

for i in data[0].split("+"):
    result += int(i)

for i in data[1:]:
    for j in i.split("+"):
        result -= int(j)

print(result)