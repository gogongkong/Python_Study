'''
https://www.acmicpc.net/problem/2828
'''


n, m = map(int, input().split())
j = int(input())

apples = []
for _ in range(j):
    apples.append(int(input()))

result = 0 # 정답을 담을 변수
now = 1 # 현재 위치

for apple in apples:
    if now <= apple and now + (m-1) >= apple:
        continue
    elif now > apple:
        result += now - apple
        now = apple
    else:
        result += apple - (now +(m-1))
        now = apple - (m-1)

print(result)

