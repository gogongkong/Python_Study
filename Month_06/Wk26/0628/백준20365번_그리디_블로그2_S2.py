'''
https://www.acmicpc.net/problem/20365
'''

'''
해결 : B
미해결 : R

문제의 수 1 <= N <= 500000
'''

n = int(input())

data = input()

dict = {'B' : 1, 'R' : 1}

dict[data[0]] += 1

for i in range(1, n):
    if data[i] != data[i-1]:
        dict[data[i]] += 1

result = min(dict['B'], dict['R'])

print(result)