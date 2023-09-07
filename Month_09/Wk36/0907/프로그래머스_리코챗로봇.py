'''
https://school.programmers.co.kr/learn/courses/30/lessons/169199
'''
from collections import deque
board1 = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
board2 = [".D.R", "....", ".G..", "...D"]

def solution(board):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = 0
    row = len(board)
    col = len(board[0])
    for x in range(row):
        for y in range(col):
            if board[x][y] == "R":
                rx, ry = x, y

    def bfs():
        visited =[[0] * col for _ in range(row)]
        visited[rx][ry] = 1
        queue = deque()
        queue.append((rx,ry))
        while queue:
            x, y = queue.popleft()
            if board[x][y] == "G":
                return visited[x][y]
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == "D":
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx < 0 or nx >= row or ny < 0 or ny >= col:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return -1
    answer = bfs()
    if answer > 0:
        answer -= 1
    return answer

print(solution(board1))
print(solution(board2))