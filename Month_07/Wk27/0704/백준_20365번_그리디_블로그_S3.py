'''
https://www.acmicpc.net/problem/20365
'''

n = int(input())

data = input()

dict = {'B' : 1, 'R' : 1}

dict[data[0]] += 1

for i in range(1, n):
    if data[i] != data[i-1]:
        dict[data[i]] +=1

print(dict)
