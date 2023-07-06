'''
https://www.acmicpc.net/problem/9465
'''

tc = int(input()) # TC의 갯수 입력

result = [] # 결과를 입력받을 리스트

for _ in range(tc): # TC 갯수만큼 반복
    n = int(input())
    S1 = list(map(int, input().split())) # 스티커 입력
    S2 = list(map(int, input().split()))

    for i in range(1, n):
        if i == 1:
            S1[1] += S2[0]
            S2[1] += S1[0]
        else:
            S1[i] = max(S2[i-1], S2[i-2]) + S1[i]
            S2[i] = max(S1[i-1], S1[i-2]) + S2[i]

    result.append(max(S1[n-1], S2[n-1]))

for i in result:
    print(i)
