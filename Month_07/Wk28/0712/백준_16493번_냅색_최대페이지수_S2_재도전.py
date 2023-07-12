'''
https://www.acmicpc.net/problem/16493
'''

'''
남은 기간 N일 
N일간 읽을 수 있는 최대 페이지 수

남은기간 N, 챕터의 수 M
챕터당 소요일수(소모값), 페이지수(이득)
'''

n, m = map(int, input().split())

date = [0]
chapter = [0]

for _ in range(m):
    a, b = map(int, input().split()) # a 챕터당 소요일 수(소모값), b 페이지 수(이득)
    date.append(a)
    chapter.append(b)

result = [ [0] * (n+1) for _ in range(m+1)]

for i in range(m+1):
    for j in range(n+1):
        if date[i] <= j:
            result[i][j] = max(result[i-1][j], result[i-1][j - date[i]] + chapter[i])
        else:
            result[i][j] = result[i-1][j]

print(result[-1][-1])