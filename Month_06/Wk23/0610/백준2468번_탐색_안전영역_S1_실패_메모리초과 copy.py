'''
https://www.acmicpc.net/problem/2468
'''
from collections import deque
import copy
import sys
sys.setrecursionlimit(10**6)
n = int(input()) # 가로, 세로 크기

data = [list(map(int, input().split())) for _ in range(n)] # 전체 지형을 입력 받을 리스트

height = max(max(data)) # 최고 높이


def dfs(x,y,data,i):
    if x < 0 or y < 0 or x >= n or y >= n or data[x][y] - i < 1:
        return False
    elif data[x][y] > 0:
        data[x][y] = 0
        dfs(x+1,y,data_copy,i)
        dfs(x,y+1,data_copy,i)
        dfs(x-1,y,data_copy,i)
        dfs(x,y-1,data_copy,i)
        return True
    return False

result = []

for i in range(0,height):
    count = 0
    data_copy = copy.deepcopy(data)
    for x in range(n):
        for y in range(n):
            if dfs(x,y,data_copy,i):
                count += 1
    result.append(count)

print(max(result))

