'''
https://www.acmicpc.net/problem/1343
'''

'''
조각은 2개
AAAA
BB
'''

data = input()

data = data.replace("XXXX", "AAAA")
data = data.replace("XX", "BB")

if "X" in data:
    print(-1)
else:
    print(data)