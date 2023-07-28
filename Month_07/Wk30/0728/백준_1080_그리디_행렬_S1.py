'''
https://www.acmicpc.net/problem/1080
'''

# 3x3 뒤집기 함수 convert
def convert(i, j, data):
    for x in range(i, i+3):
        for y in range(j, j+3):
            data[x][y] = 1- data[x][y]

n, m = map(int, input().split())

data = [list(map(int,input())) for _ in range(n)]
result = [list(map(int,input())) for _ in range(n)]
count = 0

for i in range(n-2):
    for j in range(m-2):
        if data[i][j] != result[i][j]:
            convert(i,j,data)
            count += 1

check = 0
for i in range(n):
    for j in range(m):
        if data[i][j] != result[i][j]:
            check += 1
            break

if check == 1:
    print(-1)
else:
    print(count)