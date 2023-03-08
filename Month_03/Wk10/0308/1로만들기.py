# 정수 x 입력
x = int(input())

# DP 테이블 작성
d = [0] * 100001

# 다이나믹 프로그래밍!
d[1] = 0
d[2] = 1
for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])