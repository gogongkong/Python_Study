'''
https://www.acmicpc.net/problem/1018
'''

# 체스판의 크기
m, n = map(int, input().split())
# 체스판 입력
data = [list(input()) for _ in range(m)]

result = []

for i in range(m-7):
    for j in range(n-7):
        check_1 = 0
        check_2 = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if data[x][y] == "B":
                        check_1 += 1
                    if data[x][y] == "W":
                        check_2 += 1
                else:
                    if data[x][y] == "W":
                        check_1 += 1
                    if data[x][y] == "B":
                        check_2 += 1
        result.append(check_1)
        result.append(check_2)

print(min(result))