'''
https://www.acmicpc.net/problem/6593
'''

from collections import deque
import sys

input = sys.stdin.readline

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

data = []


def bfs(x,y,z):
    visited[x][y][z] = 1
    queue = deque()
    queue.append([x,y,z])

    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if data[nx][ny][nz] == "E":
                    print("Escaped in {0} minute(s).".format(visited[x][y][z]))
                    return
                if data[nx][ny][nz] == "." and visited[nx][ny][nz] == 0:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    queue.append([nx, ny, nz])

    print("Trapped!")

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    for _ in range(L):
        data.append([list(input()) for _ in range(R)])
        temp = input()
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    
    for z in range(L):
        for x in range(R):
            for y in range(C):
                if data[z][x][y] == "S":
                    bfs(x,y,z)
                

                