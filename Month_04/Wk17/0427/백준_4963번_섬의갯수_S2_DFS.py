'''
https://www.acmicpc.net/problem/4963
'''
# 풀이 방식 : DFS

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x,y):
    if x < 0 or y < 0 or x >=h or y>=w or data[x][y] == 0:
        return False
    if data[x][y] == 1:
        data[x][y] += 1
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y+1)
        dfs(x-1,y-1)
        dfs(x+1,y-1)
        dfs(x-1,y+1)

        return True
    return False

result = []

while True:
    count = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0: # TC 종료
        break
    data = [list(map(int, input().split())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                count +=1
    result.append(count)

for i in result:
    print(i)

