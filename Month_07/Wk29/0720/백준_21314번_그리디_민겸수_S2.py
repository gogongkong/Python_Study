'''
https://www.acmicpc.net/problem/21314
'''

datas = input()

max_value = ''
min_value = ''
m = 0

for data in datas:
    if data == 'K':
        if m > 0:
            max_value += str(10 ** m * 5)
            min_value += str(10 ** m + 5)
            m = 0
        else: #m == 0
            max_value += '5'
            min_value += '5'
    else: # data = M
        m += 1

if m > 0:
    max_value += str(10 ** m)
    min_value += str(10 ** m)

print(max_value)
print(min_value)
    