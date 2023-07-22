'''
https://www.acmicpc.net/problem/1012
'''

tc = int(input())

for _ in range(tc):

    m, n, k = map(int, input().split())
    visited = [False] * (k+1)
    data = [[0] * (n+1) for _ in range(m+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        data[a][b] = 1
    print(data)