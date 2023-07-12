'''
https://www.acmicpc.net/problem/11052
'''

'''
1장만 사는 경우 == d[1]
d[1] = p1 + d[0]

2장만 사는 경우
d[2] = d[1] + p1, d[0] + p2

3장만 사는 경우
d[3] = d[2] + p1, d[1] + p2, d[0] + p3

4장만 사는 경우
d[4] = d[3] + p1, d[2] + p2, d[1] + p3, d[0] + p4

d[i] = max(d[i-1] + p1, d[i-2] + p2, d[i-3] + p3 ..... d[i-j] + pj

점화식 유추
== d[i] = max(d[i], d[i-j] + p[j])
'''

# 카드 갯수 입력
n = int(input())
# 카드의 갯수에 따른 가격 입력
p = [0] + list(map(int, input().split()))
# dp 테이블 선언 및 초기화
d = [0 for _ in range(n+1)]

d[1] = p[1]

for i in range(2, n+1):
    for j in range(1,i+1):
        d[i] = max(d[i], d[i-j] + p[j])
        
print(d[-1])