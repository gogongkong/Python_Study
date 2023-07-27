'''
https://www.acmicpc.net/problem/1080
'''

n, m = map(int, input().split())

data = [list(map(int, input())) for _ in range(n)]
answer = [list(map(int, input())) for _ in range(n)]

def convert(i,j): # 3 x 3변환 함수
    for x in range(i+3):
        for y in range(j+3):
            data[x][y] = 1 - data[x][y]

count = 0

# -2 를 하는 이유는 3X3이기때문에 기준칸 1x1에서 두칸이상 벗어날 수 없기때문
for i in range(n-2):
    for j in range(m-2):
        # 해당 칸이 다를 경우
        if data[i][j] != answer[i][j]:
            convert(i,j)
            count +=1

check = 0
# 정답과 맞는 지확인
for i in range(n):
    for j in range(m):
        if data[i][j] != answer[i][j]:
            check = 1
            break

if check == 1:
    print(-1)
else:
    print(count)