'''
https://www.acmicpc.net/problem/1080
'''

n,m = map(int, input().split())

data = [list(int(input())) for _ in range(m)]
result = [list(int(input())) for _ in range(m)]

def convert(i,j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            data[x][y] += 1 - data[x][y]

first = 0
sec = 0

for i in range(m-2):
    for j in range(n-2):

        