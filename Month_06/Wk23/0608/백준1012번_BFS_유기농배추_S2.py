'''
https://www.acmicpc.net/problem/1012
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
tc = int(input()) # TestCase 갯수

def dfs(x,y):
    if x < 0 or y <0 or x >= m or y >= n or data[x][y] == 0:
        return False
    elif data[x][y] == 1:
        data[x][y] = 0
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

result = []

for _ in range(tc):
    count = 0
    m, n, k = map(int, input().split()) # 가로, 세로, 배추위치
    data = [[0] * (n+1) for i in range(m+1)]
    for _ in range(k): # 배추 위치 입력
        a, b = map(int, input().split())
        data[a][b] = 1
    for i in range(m):
        for j in range(n):
            if dfs(i,j):
                count +=1
    result.append(count)

for i in result:
    print(i)



