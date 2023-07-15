'''
https://www.acmicpc.net/problem/2828
'''

n, m = map(int, input().split())

j = int(input())

apples = []
for _ in range(j):
    apples.append(int(input()))

result = 0
now = 1
    
# Case 01 : 현재위치 <= 사과 <= 바구니의 끝(now + m)
# Case 02 : 사과 < 현재위치 < 바구니의 끝(now + m)
# Case 03 : 현재위치 < 바구니의 끝 < 사과

for apple in apples:
    if now <= apple <= now + (m-1):
        continue
    elif apple < now:
        result += now - apple
    else:
        result += apple - (now + (m-1))

print(result)