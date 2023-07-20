'''
https://www.acmicpc.net/problem/21314
'''

datas = list(input())

max_data = ''
min_data = ''
m = 0

for data in datas:
    if data == 'K':
        if m > 0:
            max_data += str(10 ** m * 5)
            min_data += str(10 ** m + 5)
            m = 0
        else: # m == 0
            max_data += '5'
            min_data += '5'
    else: # data =='M'
        m += 1

print(max_data)
print(min_data)