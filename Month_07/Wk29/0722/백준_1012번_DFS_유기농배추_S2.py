'''
https://www.acmicpc.net/problem/1012
'''
from collections import deque

def dfs(x,y, data):
    if data[x][y] == 1:
        data[x][y] = 0
        dfs(x+1,y,data)
        dfs(x,y+1,data)
        dfs(x-1,y,data)
        dfs(x,y-1,data)
        

tc = int(input())

for _ in range(tc):

    m, n, k = map(int, input().split())
    data = [[0] * (n+1) for _ in range(m+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        data[a][b] = 1
    result = 0
    for x in range(m):
        for y in range(n):
            if data[x][y] == 1:
                dfs(x, y, data)
                result += 1
    print(result)

